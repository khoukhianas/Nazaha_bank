<template>
  <div class="dashboard">
    <!-- Section des cartes de statistiques -->
    <div class="row mb-4">
      <div class="col-md-3">
        <div class="card text-center shadow-sm">
          <div class="card-body">
            <i class="bi bi-people-fill text-primary fs-2"></i>
            <h5 class="card-title mt-2">Utilisateurs</h5>
            <h3 class="card-text">{{ stats.users }}</h3>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card text-center shadow-sm">
          <div class="card-body">
            <i class="bi bi-piggy-bank text-success fs-2"></i>
            <h5 class="card-title mt-2">Comptes</h5>
            <h3 class="card-text">{{ stats.accounts }}</h3>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card text-center shadow-sm">
          <div class="card-body">
            <i class="bi bi-cash-stack text-warning fs-2"></i>
            <h5 class="card-title mt-2">Revenus</h5>
            <h3 class="card-text">{{ stats.revenue }} €</h3>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card text-center shadow-sm">
          <div class="card-body">
            <i class="bi bi-graph-up text-danger fs-2"></i>
            <h5 class="card-title mt-2">Transactions</h5>
            <h3 class="card-text">{{ stats.transactions }}</h3>
          </div>
        </div>
      </div>
    </div>

    <!-- Section des graphiques -->
    <div class="row">
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Types de comptes</h5>
            <canvas id="accountChart"></canvas>
          </div>
        </div>
      </div>
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Activité récente</h5>
            <canvas id="activityChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
  name: "DashboardPage",
  data() {
    return {
      stats: {
        users: 1200,
        accounts: 950,
        revenue: 50000,
        transactions: 3000,
      },
    };
  },
  mounted() {
    // Graphique des types de comptes
    new Chart(document.getElementById("accountChart"), {
      type: "doughnut",
      data: {
        labels: ["Courant", "Épargne", "Entreprise"],
        datasets: [
          {
            data: [500, 300, 150],
            backgroundColor: ["#007bff", "#28a745", "#ffc107"],
          },
        ],
      },
    });

    // Graphique de l'activité récente
    new Chart(document.getElementById("activityChart"), {
      type: "bar",
      data: {
        labels: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
        datasets: [
          {
            label: "Transactions",
            data: [400, 500, 600, 700, 800, 900],
            backgroundColor: "#dc3545",
          },
        ],
      },
    });
  },
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
  background-color: #f8f9fa; /* Couleur de fond */
}

.card {
  border: none;
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: scale(1.05); /* Zoom au survol */
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

.card-title {
  font-size: 1.25rem;
  font-weight: 500;
}

.card-text {
  font-size: 1.5rem;
  font-weight: bold;
}

/* Graphiques */
canvas {
  max-width: 100%;
  height: 250px;
}
</style>
