<template>
  <div class="admin-support">
    <h2>Support Client</h2>
    <p>Réponses aux demandes des clients.</p>
    <ul>
      <!-- Utilisation de `index` -->
      <li v-for="(ticket, index) in tickets" :key="index">
        <strong>{{ ticket.subject }}</strong> - {{ ticket.status }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "AdminSupport",
  data() {
    return {
      // Exemple de données fictives (remplacez par les données backend)
      tickets: [
        { subject: "Problème de connexion", status: "En cours" },
        { subject: "Erreur de paiement", status: "Résolu" },
        { subject: "Demande d'informations", status: "En attente" },
      ],
    };
  },
};
</script>

<style scoped>
.admin-support {
  padding: 20px;
}
</style>
