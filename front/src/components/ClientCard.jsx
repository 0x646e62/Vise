import {
  CreditCard,
  Crown,
  DollarSign,
  Edit,
  MapPin,
  Trash2,
} from "lucide-react";
import toast from "react-hot-toast";
import { clientesService } from "../services/api";

const ClientCard = ({ client, onClientUpdated, onEdit }) => {
  const handleDelete = async () => {
    if (window.confirm("¿Estás seguro de que quieres eliminar este cliente?")) {
      try {
        await clientesService.delete(client.clientId);
        toast.success("Cliente eliminado exitosamente");
        onClientUpdated();
      } catch (error) {
        const message =
          error.response?.data?.detail || "Error al eliminar el cliente";
        toast.error(message);
      }
    }
  };

  const formatCurrency = (amount) => {
    return new Intl.NumberFormat("es-ES", {
      style: "currency",
      currency: "USD",
    }).format(amount);
  };

  const getCardTypeColor = (cardType) => {
    const colors = {
      Standard: "#6b7280",
      Gold: "#fbbf24",
      Platinum: "#e5e7eb",
      Black: "#1f2937",
    };
    return colors[cardType] || "#6b7280";
  };

  return (
    <div className="client-card">
      <div className="client-header">
        <div>
          <div className="client-name">{client.name}</div>
          <div className="client-id">ID: {client.clientId}</div>
        </div>
        <div className="client-actions">
          <button
            onClick={() => onEdit(client)}
            className="btn btn-secondary"
            style={{ padding: "0.5rem", minWidth: "auto" }}
            title="Editar cliente"
          >
            <Edit size={16} />
          </button>
          <button
            onClick={handleDelete}
            className="btn btn-danger"
            style={{ padding: "0.5rem", minWidth: "auto" }}
            title="Eliminar cliente"
          >
            <Trash2 size={16} />
          </button>
        </div>
      </div>

      <div className="client-info">
        <div className="info-row">
          <span className="info-label">
            <MapPin
              size={16}
              style={{ display: "inline", marginRight: "0.5rem" }}
            />
            País
          </span>
          <span className="info-value">{client.country}</span>
        </div>

        <div className="info-row">
          <span className="info-label">
            <DollarSign
              size={16}
              style={{ display: "inline", marginRight: "0.5rem" }}
            />
            Ingresos
          </span>
          <span className="info-value">
            {formatCurrency(client.monthlyIncome)}
          </span>
        </div>

        <div className="info-row">
          <span className="info-label">
            <CreditCard
              size={16}
              style={{ display: "inline", marginRight: "0.5rem" }}
            />
            Tarjeta
          </span>
          <span
            className="badge"
            style={{
              backgroundColor: getCardTypeColor(client.cardType) + "20",
              color: getCardTypeColor(client.cardType),
              border: `1px solid ${getCardTypeColor(client.cardType)}30`,
            }}
          >
            {client.cardType}
          </span>
        </div>

        <div className="info-row">
          <span className="info-label">
            <Crown
              size={16}
              style={{ display: "inline", marginRight: "0.5rem" }}
            />
            Club Vise
          </span>
          <span
            className={`badge ${
              client.viseClub ? "badge-success" : "badge-secondary"
            }`}
          >
            {client.viseClub ? "Miembro" : "No miembro"}
          </span>
        </div>

        {client.status && (
          <div className="info-row">
            <span className="info-label">Estado</span>
            <span className="badge badge-success">{client.status}</span>
          </div>
        )}
      </div>
    </div>
  );
};

export default ClientCard;
