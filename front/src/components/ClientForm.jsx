import { zodResolver } from "@hookform/resolvers/zod";
import { Plus, X } from "lucide-react";
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import toast from "react-hot-toast";
import { z } from "zod";
import { clientesService } from "../services/api";

const clientSchema = z.object({
  name: z
    .string()
    .min(2, "El nombre debe tener al menos 2 caracteres")
    .max(50, "El nombre no puede superar 50 caracteres"),
  country: z
    .string()
    .min(2, "El país debe tener al menos 2 caracteres")
    .max(50, "El país no puede superar 50 caracteres"),
  monthlyIncome: z.number().min(0, "Los ingresos deben ser positivos"),
  viseClub: z.boolean(),
  cardType: z
    .string()
    .min(2, "El tipo de tarjeta debe tener al menos 2 caracteres")
    .max(50, "El tipo de tarjeta no puede superar 50 caracteres"),
});

const ClientForm = ({ onClientAdded, editingClient, onEditComplete }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
    setValue,
    watch,
  } = useForm({
    resolver: zodResolver(clientSchema),
    defaultValues: {
      name: "",
      country: "",
      monthlyIncome: 0,
      viseClub: false,
      cardType: "Standard",
    },
  });

  React.useEffect(() => {
    if (editingClient) {
      setValue("name", editingClient.name);
      setValue("country", editingClient.country);
      setValue("monthlyIncome", editingClient.monthlyIncome);
      setValue("viseClub", editingClient.viseClub);
      setValue("cardType", editingClient.cardType);
      setIsOpen(true);
    }
  }, [editingClient, setValue]);

  const onSubmit = async (data) => {
    setIsSubmitting(true);
    try {
      if (editingClient) {
        await clientesService.update(editingClient.clientId, data);
        toast.success("Cliente actualizado exitosamente");
        onEditComplete();
      } else {
        await clientesService.create(data);
        toast.success("Cliente creado exitosamente");
        onClientAdded();
      }

      reset();
      setIsOpen(false);
    } catch (error) {
      const message =
        error.response?.data?.detail || "Error al procesar la solicitud";
      toast.error(message);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleClose = () => {
    setIsOpen(false);
    reset();
    if (editingClient && onEditComplete) {
      onEditComplete();
    }
  };

  const cardTypes = ["Standard", "Gold", "Platinum", "Black"];

  return (
    <>
      {!editingClient && (
        <button onClick={() => setIsOpen(true)} className="btn btn-primary">
          <Plus size={20} />
          Agregar Cliente
        </button>
      )}

      {isOpen && (
        <div
          className="modal-overlay"
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: "rgba(0, 0, 0, 0.5)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 1000,
          }}
        >
          <div
            className="modal-content"
            style={{
              backgroundColor: "white",
              borderRadius: "12px",
              padding: "2rem",
              width: "90%",
              maxWidth: "500px",
              maxHeight: "90vh",
              overflowY: "auto",
            }}
          >
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "1.5rem",
              }}
            >
              <h2 style={{ margin: 0, fontSize: "1.5rem", fontWeight: "700" }}>
                {editingClient ? "Editar Cliente" : "Agregar Nuevo Cliente"}
              </h2>
              <button
                onClick={handleClose}
                style={{
                  background: "none",
                  border: "none",
                  cursor: "pointer",
                  padding: "0.5rem",
                  borderRadius: "4px",
                }}
              >
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleSubmit(onSubmit)}>
              <div className="form-group">
                <label htmlFor="name">Nombre *</label>
                <input
                  {...register("name")}
                  type="text"
                  id="name"
                  placeholder="Ingrese el nombre completo"
                />
                {errors.name && (
                  <span
                    style={{
                      color: "#dc2626",
                      fontSize: "0.875rem",
                      marginTop: "0.25rem",
                    }}
                  >
                    {errors.name.message}
                  </span>
                )}
              </div>

              <div className="form-group">
                <label htmlFor="country">País *</label>
                <input
                  {...register("country")}
                  type="text"
                  id="country"
                  placeholder="Ingrese el país"
                />
                {errors.country && (
                  <span
                    style={{
                      color: "#dc2626",
                      fontSize: "0.875rem",
                      marginTop: "0.25rem",
                    }}
                  >
                    {errors.country.message}
                  </span>
                )}
              </div>

              <div className="form-group">
                <label htmlFor="monthlyIncome">Ingresos Mensuales *</label>
                <input
                  {...register("monthlyIncome", { valueAsNumber: true })}
                  type="number"
                  id="monthlyIncome"
                  placeholder="Ingrese los ingresos mensuales"
                  min="0"
                />
                {errors.monthlyIncome && (
                  <span
                    style={{
                      color: "#dc2626",
                      fontSize: "0.875rem",
                      marginTop: "0.25rem",
                    }}
                  >
                    {errors.monthlyIncome.message}
                  </span>
                )}
              </div>

              <div className="form-group">
                <label htmlFor="cardType">Tipo de Tarjeta *</label>
                <select {...register("cardType")} id="cardType">
                  {cardTypes.map((type) => (
                    <option key={type} value={type}>
                      {type}
                    </option>
                  ))}
                </select>
                {errors.cardType && (
                  <span
                    style={{
                      color: "#dc2626",
                      fontSize: "0.875rem",
                      marginTop: "0.25rem",
                    }}
                  >
                    {errors.cardType.message}
                  </span>
                )}
              </div>

              <div className="checkbox-group">
                <input
                  {...register("viseClub")}
                  type="checkbox"
                  id="viseClub"
                />
                <label htmlFor="viseClub">Miembro del Club Vise</label>
              </div>

              <div style={{ display: "flex", gap: "1rem", marginTop: "2rem" }}>
                <button
                  type="submit"
                  className="btn btn-primary"
                  disabled={isSubmitting}
                  style={{ flex: 1 }}
                >
                  {isSubmitting
                    ? "Guardando..."
                    : editingClient
                    ? "Actualizar"
                    : "Crear Cliente"}
                </button>
                <button
                  type="button"
                  onClick={handleClose}
                  className="btn btn-secondary"
                >
                  Cancelar
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
};

export default ClientForm;
