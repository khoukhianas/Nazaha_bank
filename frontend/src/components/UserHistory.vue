<template>
    <div>
      <h2>Historique des Transactions</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Date</th>
            <th>Description</th>
            <th>Montant</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transaction in transactions" :key="transaction.id">
            <td>{{ transaction.date }}</td>
            <td>{{ transaction.description }}</td>
            <td>{{ transaction.amount }} €</td>
            <td>{{ transaction.type }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserHistory",
    data() {
      return {
        transactions: [
          { id: 1, date: "2024-12-01", description: "Virement interne", amount: 200, type: "Débit" },
          { id: 2, date: "2024-12-02", description: "Paiement en ligne", amount: 50, type: "Débit" },
          { id: 3, date: "2024-12-03", description: "Transfert externe", amount: 300, type: "Crédit" },
        ],
      };
    },
  };
  </script>
  