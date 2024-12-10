<template>
  <div class="admin-transactions">
    <h2>Transactions</h2>
    <p>Historique des transactions réalisées.</p>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>#</th>
          <th>Date</th>
          <th>Montant</th>
          <th>Type</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(transaction, index) in transactions" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ transaction.date }}</td>
          <td>{{ transaction.amount }} €</td>
          <td>{{ transaction.type }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "AdminTransactions",
  data() {
    return {
      // Exemple de données fictives (remplacez par les données backend)
      transactions: [
        { date: "2023-12-01", amount: 150, type: "Crédit" },
        { date: "2023-12-02", amount: 200, type: "Débit" },
        { date: "2023-12-03", amount: 300, type: "Crédit" },
      ],
    };
  },
};
</script>

<style scoped>
.admin-transactions {
  padding: 20px;
}
</style>
