<template>
    <div>
      <h2>Virement Interne</h2>
      <form @submit.prevent="submitTransfer">
        <div class="mb-3">
          <label for="fromAccount" class="form-label">Compte Source</label>
          <select v-model="transfer.fromAccount" class="form-select">
            <option value="Compte Courant">Compte Courant</option>
            <option value="Compte Épargne">Compte Épargne</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="toAccount" class="form-label">Compte Destinataire</label>
          <select v-model="transfer.toAccount" class="form-select">
            <option value="Compte Courant">Compte Courant</option>
            <option value="Compte Épargne">Compte Épargne</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="amount" class="form-label">Montant</label>
          <input type="number" v-model="transfer.amount" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Effectuer le Virement</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserTransfer",
    data() {
      return {
        transfer: {
          fromAccount: "",
          toAccount: "",
          amount: 0,
        },
      };
    },
    methods: {
      submitTransfer() {
        console.log("Virement Interne :", this.transfer);
        alert("Virement effectué avec succès !");
      },
    },
  };
  </script>
  