<template>
    <div>
      <h2>Transfert Externe</h2>
      <form @submit.prevent="submitExternalTransfer">
        <div class="mb-3">
          <label for="toRecipient" class="form-label">Destinataire</label>
          <input type="text" v-model="externalTransfer.toRecipient" class="form-control" placeholder="Nom du destinataire" />
        </div>
        <div class="mb-3">
          <label for="bankDetails" class="form-label">Détails Bancaires</label>
          <input type="text" v-model="externalTransfer.bankDetails" class="form-control" placeholder="IBAN ou numéro de compte" />
        </div>
        <div class="mb-3">
          <label for="amount" class="form-label">Montant</label>
          <input type="number" v-model="externalTransfer.amount" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Effectuer le Transfert</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserExternalTransfer",
    data() {
      return {
        externalTransfer: {
          toRecipient: "",
          bankDetails: "",
          amount: 0,
        },
      };
    },
    methods: {
      submitExternalTransfer() {
        console.log("Transfert Externe :", this.externalTransfer);
        alert("Transfert effectué avec succès !");
      },
    },
  };
  </script>
  