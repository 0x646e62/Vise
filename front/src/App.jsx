import { RefreshCw, Users } from "lucide-react";
import { useEffect, useState } from "react";
import { Toaster } from "react-hot-toast";
import ClientCard from "./components/ClientCard";
import ClientForm from "./components/ClientForm";
import { clientesService } from "./services/api";

function App() {
  const [clients, setClients] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingClient, setEditingClient] = useState(null);

  const fetchClients = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await clientesService.getAll();
      setClients(data);
    } catch (error) {
      console.error("Error fetching clients:", error);
      setError(
        "Error al cargar los clientes. Verifica que la API esté funcionando."
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchClients();
  }, []);

  const handleClientAdded = () => {
    fetchClients();
  };

  const handleClientUpdated = () => {
    fetchClients();
  };

  const handleEdit = (client) => {
    setEditingClient(client);
  };

  const handleEditComplete = () => {
    setEditingClient(null);
    fetchClients();
  };

  return (
    <div className="container">
      <Toaster position="top-right" />

      <header className="header">
        <h1>Vise - Gestión de Clientes</h1>
        <p>Sistema de administración de clientes y tarjetas</p>
      </header>

      <div className="card">
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "1.5rem",
            flexWrap: "wrap",
            gap: "1rem",
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
            <Users size={24} />
            <h2 style={{ margin: 0, fontSize: "1.5rem", fontWeight: "700" }}>
              Clientes ({clients.length})
            </h2>
          </div>

          <div style={{ display: "flex", gap: "1rem" }}>
            <button
              onClick={fetchClients}
              className="btn btn-secondary"
              disabled={loading}
            >
              <RefreshCw size={20} className={loading ? "animate-spin" : ""} />
              Actualizar
            </button>
            <ClientForm
              onClientAdded={handleClientAdded}
              editingClient={editingClient}
              onEditComplete={handleEditComplete}
            />
          </div>
        </div>

        {error && (
          <div className="error-message">
            <strong>Error:</strong> {error}
            <button
              onClick={fetchClients}
              style={{
                marginLeft: "1rem",
                background: "none",
                border: "none",
                color: "#dc2626",
                textDecoration: "underline",
                cursor: "pointer",
              }}
            >
              Reintentar
            </button>
          </div>
        )}

        {loading ? (
          <div className="loading">
            <RefreshCw
              size={24}
              style={{ animation: "spin 1s linear infinite" }}
            />
            Cargando clientes...
          </div>
        ) : clients.length === 0 ? (
          <div className="empty-state">
            <Users size={48} style={{ opacity: 0.5, marginBottom: "1rem" }} />
            <h3>No hay clientes registrados</h3>
            <p>
              Comienza agregando tu primer cliente usando el botón "Agregar
              Cliente"
            </p>
          </div>
        ) : (
          <div className="clients-grid">
            {clients.map((client) => (
              <ClientCard
                key={client.clientId}
                client={client}
                onClientUpdated={handleClientUpdated}
                onEdit={handleEdit}
              />
            ))}
          </div>
        )}
      </div>

      <style jsx>{`
        @keyframes spin {
          from {
            transform: rotate(0deg);
          }
          to {
            transform: rotate(360deg);
          }
        }
        .animate-spin {
          animation: spin 1s linear infinite;
        }
      `}</style>
    </div>
  );
}

export default App;
