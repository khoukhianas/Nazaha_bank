<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-light">
      <a class="navbar-brand" href="#">
        <img src="/images/NB.png" alt="Logo" style="height: 50px;" />
        NazahaBank
      </a>
    </nav>

    <!-- SignIn Form Section -->
    <div class="auth-form-container">
      <div class="auth-form">
        <h2>Sign In</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label>Email Address:</label>
            <input
              type="email"
              v-model="email"
              placeholder="Email Address"
              required
            />
            <span v-if="errors.email" class="error">{{ errors.email }}</span>
          </div>
          <div class="form-group">
            <label>Password:</label>
            <input
              type="password"
              v-model="password"
              placeholder="Password"
              required
            />
            <span v-if="errors.password" class="error">{{ errors.password }}</span>
          </div>
          <button
            type="submit"
            :disabled="!isFormValid || isLoading"
          >
            <span v-if="isLoading">Signing In...</span>
            <span v-else>Sign In</span>
          </button>
        </form>
        <div class="additional-links">
          <p>
            Don't have an account?
            <router-link to="/signup">Sign Up</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignIn",
  data() {
    return {
      email: "",
      password: "",
      errors: {}, // Object to store validation errors
      isLoading: false, // Tracks the loading state
    };
  },
  computed: {
    isFormValid() {
      return this.validateEmail(this.email) && this.password.length >= 6;
    },
  },
  methods: {
    validateEmail(email) {
      const re = /\S+@\S+\.\S+/;
      return re.test(email);
    },
    async submitForm() {
      if (!this.isFormValid) {
        alert("Please fill out the form correctly.");
        return;
      }

      this.isLoading = true; // Start loading state

      try {
        const response = await axios.post("http://localhost:8000/api/signin", {
          email: this.email,
          password: this.password,
        });
        alert(response.data.message); // Show success message
        localStorage.setItem("authToken", response.data.token); // Save token
        this.$router.push("/dashboard"); // Redirect to a dashboard or home page
      } catch (error) {
        if (error.response && error.response.data) {
          this.errors = error.response.data.errors || {};
          alert(error.response.data.error || "An error occurred during sign in.");
        } else {
          alert("An error occurred during sign in.");
        }
      } finally {
        this.isLoading = false; // End loading state
      }
    },
  },
};
</script>

<style scoped>
.navbar {
  transition: background-color 0.3s ease;
}
.navbar-brand img {
  height: 50px;
}
.auth-form-container {
  margin-top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 100px);
  background-color: #f9f9f9;
}
.auth-form {
  width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
.auth-form h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}
.form-group {
  margin-bottom: 15px;
}
.form-group label {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
}
.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
button {
  width: 100%;
  padding: 10px;
  color: white;
  background-color: #0066cc;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
}
button:hover:not(:disabled) {
  background-color: #0056b3;
}
.additional-links {
  text-align: center;
  margin-top: 15px;
}
.additional-links a {
  color: #0066cc;
  text-decoration: none;
}
.additional-links a:hover {
  text-decoration: underline;
}
.error {
  color: red;
  font-size: 0.8em;
}
</style>
