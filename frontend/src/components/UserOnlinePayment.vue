<template>
    <div>
      <h2>Paiement en Ligne</h2>
      <form @submit.prevent="submitPayment">
        <div class="mb-3">
          <label for="merchant" class="form-label">Marchand</label>
          <input type="text" v-model="payment.merchant" class="form-control" placeholder="Nom du marchand" />
        </div>
        <div class="mb-3">
          <label for="amount" class="form-label">Montant</label>
          <input type="number" v-model="payment.amount" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="paymentMethod" class="form-label">Mode de Paiement</label>
          <select v-model="payment.paymentMethod" class="form-select">
            <option value="Carte Bancaire">Carte Bancaire</option>
            <option value="Compte Bancaire">Compte Bancaire</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Effectuer le Paiement</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserOnlinePayment",
    data() {
      return {
        payment: {
          merchant: "",
          amount: 0,
          paymentMethod: "",
        },
      };
    },
    methods: {
      submitPayment() {
        console.log("Paiement en Ligne :", this.payment);
        alert("Paiement effectué avec succès !");
      },
    },
  };
  </script>
  