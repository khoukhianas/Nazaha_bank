<template>
    <div class="container mt-4">
      <h3>Paramètres</h3>
      <form @submit.prevent="saveSettings">
        <div class="mb-3">
          <label for="email" class="form-label">Email Administrateur</label>
          <input type="email" id="email" class="form-control" v-model="settings.email" />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Mot de passe</label>
          <input type="password" id="password" class="form-control" v-model="settings.password" />
        </div>
        <button type="submit" class="btn btn-primary">Enregistrer</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "AdminSettings",
    data() {
      return {
        settings: {
          email: "admin@example.com",
          password: "",
        },
      };
    },
    methods: {
      saveSettings() {
        alert("Paramètres enregistrés !");
      },
    },
  };
  </script>
  