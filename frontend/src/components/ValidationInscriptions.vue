<template>
    <div class="validation-inscriptions">
      <h3>Validation des inscriptions</h3>
      <b-table :items="requests" :fields="fields" responsive="sm">
        <template #cell(actions)="row">
          <b-button
            variant="success"
            size="sm"
            @click="acceptRequest(row.item)"
            class="mr-2"
          >
            Accepter
          </b-button>
          <b-button
            variant="danger"
            size="sm"
            @click="rejectRequest(row.item)"
          >
            Rejeter
          </b-button>
        </template>
      </b-table>
  
      <!-- Modal de confirmation -->
      <b-modal
        id="confirm-modal"
        :title="modalTitle"
        @ok="confirmAction"
        ok-title="Confirmer"
        cancel-title="Annuler"
      >
        <p>{{ modalMessage }}</p>
      </b-modal>
  
      <!-- Notification Toast -->
      <b-toast
        id="action-toast"
        :title="toastTitle"
        variant="success"
        solid
        :auto-hide-delay="3000"
      >
        {{ toastMessage }}
      </b-toast>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        requests: [
          {
            id: 1,
            name: "Jean Martin",
            email: "jean.martin@example.com",
            accountType: "Courant",
            date: "2024-12-01",
          },
          // Autres demandes...
        ],
        fields: [
          { key: "name", label: "Nom" },
          { key: "email", label: "Email" },
          { key: "accountType", label: "Type de compte" },
          { key: "date", label: "Date de demande" },
          { key: "actions", label: "Actions" },
        ],
        selectedRequest: null,
        actionType: "",
        modalTitle: "",
        modalMessage: "",
        toastTitle: "",
        toastMessage: "",
      };
    },
    methods: {
      acceptRequest(request) {
        this.selectedRequest = request;
        this.actionType = "accept";
        this.modalTitle = "Confirmer l'acceptation";
        this.modalMessage = `Êtes-vous sûr de vouloir accepter la demande de ${request.name} ?`;
        this.$bvModal.show("confirm-modal");
      },
      rejectRequest(request) {
        this.selectedRequest = request;
        this.actionType = "reject";
        this.modalTitle = "Confirmer le rejet";
        this.modalMessage = `Êtes-vous sûr de vouloir rejeter la demande de ${request.name} ?`;
        this.$bvModal.show("confirm-modal");
      },
      confirmAction() {
        if (this.actionType === "accept") {
          // Logique pour accepter la demande
          this.toastTitle = "Demande acceptée";
          this.toastMessage = `La demande de ${this.selectedRequest.name} a été acceptée avec succès.`;
        } else if (this.actionType === "reject") {
          // Logique pour rejeter la demande
          this.toastTitle = "Demande rejetée";
          this.toastMessage = `La demande de ${this.selectedRequest.name} a été rejetée.`;
        }
        // Retirer la demande de la liste
        this.requests = this.requests.filter(
          (req) => req.id !== this.selectedRequest.id
        );
        this.$bvToast.show("action-toast");
      },
    },
  };
  </script>
  
  <style scoped>
  .validation-inscriptions {
    padding: 20px;
  }
  
  h3 {
    margin-bottom: 20px;
  }
  </style>
  