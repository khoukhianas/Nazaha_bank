<template>
  <div class="admin-accounts">
    <h2>Gestion des comptes</h2>
    <p>Liste des comptes disponibles.</p>
    <ul>
      <!-- Utilisation de `index` pour la boucle -->
      <li v-for="(account, index) in accounts" :key="index">
        <!-- Nom du compte (ajustez selon les données du backend) -->
        {{ account.name || `Compte ${index + 1}` }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "AdminAccounts",
  data() {
    return {
      // Exemple de données fictives (remplacez par les données backend)
      accounts: [
        { name: "Compte Courant" },
        { name: "Compte Épargne" },
        { name: "Compte Entreprise" },
      ],
    };
  },
};
</script>

<style scoped>
.admin-accounts {
  padding: 20px;
}
</style>
