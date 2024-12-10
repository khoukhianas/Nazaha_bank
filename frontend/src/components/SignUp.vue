<template>
  <div>
    <!-- Navbar with Logo -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-light">
      <a class="navbar-brand d-flex align-items-center" href="#">
        <img src="/images/NB.png" alt="Logo" class="navbar-logo" />
        <span class="ml-2">NazahaBank</span>
      </a>
    </nav>

    <!-- Sign Up Form Section -->
    <div class="auth-form-container">
      <div class="auth-form">
        <h2>Sign Up for a Bank Account</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label>Full Name:</label>
            <input
              type="text"
              v-model="fullName"
              placeholder="Full Name"
              required
            />
            <span v-if="errors.full_name" class="error">{{ errors.full_name }}</span>
          </div>
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
            <label>CINE (National ID):</label>
            <input
              type="text"
              v-model="cine"
              @blur="formatCINE"
              placeholder="CINE (e.g., AB12345)"
              required
            />
            <span v-if="errors.cine" class="error">{{ errors.cine }}</span>
          </div>
          <div class="form-group">
            <label>Date of Birth:</label>
            <input
              type="date"
              v-model="dateOfBirth"
              @input="validateYear"
              required
            />
            <span v-if="errors.date_of_birth" class="error">
              {{ errors.date_of_birth }}
            </span>
          </div>
          <div class="form-group">
            <label>Place of Birth:</label>
            <input
              type="text"
              v-model="placeOfBirth"
              placeholder="Place of Birth"
              required
            />
            <span v-if="errors.place_of_birth" class="error">
              {{ errors.place_of_birth }}
            </span>
          </div>
          <div class="form-group">
            <label>ID Card Upload:</label>
            <input
              type="file"
              @change="handleFileUpload"
              accept=".jpg,.jpeg,.png,.pdf"
              required
            />
            <span v-if="errors.idCard" class="error">{{ errors.idCard }}</span>
          </div>
          <div class="form-group">
            <label>Password:</label>
            <input
              type="password"
              v-model="password"
              placeholder="Password"
              @input="checkPasswordStrength"
              required
            />
            <div
              class="password-strength"
              :style="{ backgroundColor: passwordStrengthColor }"
            >
              {{ passwordStrengthText }}
            </div>
            <span v-if="errors.password" class="error">{{ errors.password }}</span>
          </div>
          <div class="form-group">
            <label>Confirm Password:</label>
            <input
              type="password"
              v-model="confirmPassword"
              placeholder="Confirm Password"
              required
            />
            <span v-if="errors.confirmPassword" class="error">
              {{ errors.confirmPassword }}
            </span>
          </div>
          <button type="submit" :disabled="!isFormValid">Sign Up</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      fullName: "",
      email: "",
      cine: "",
      dateOfBirth: "",
      placeOfBirth: "",
      idCardFile: null,
      password: "",
      confirmPassword: "",
      passwordStrengthText: "",
      passwordStrengthColor: "#ccc",
      errors: {}, // Object to hold validation errors
    };
  },
  computed: {
    isFormValid() {
      return (
        this.fullName &&
        this.validateEmail(this.email) &&
        this.validateCINE(this.cine) &&
        this.dateOfBirth &&
        this.placeOfBirth &&
        this.idCardFile &&
        this.password.length >= 8 &&
        this.password === this.confirmPassword
      );
    },
  },
  methods: {
    validateEmail(email) {
      const re = /\S+@\S+\.\S+/;
      return re.test(email);
    },
    validateCINE(cine) {
      const re = /^[A-Z]{2}\d{5,6}$/;
      return re.test(cine);
    },
    formatCINE() {
      if (this.cine) {
        this.cine = this.cine.toUpperCase().replace(/[^A-Z0-9]/g, "");
      }
    },
    validateYear() {
      const year = this.dateOfBirth.split("-")[0];
      if (year.length > 4) {
        this.errors.date_of_birth = "Year must have 4 digits.";
      } else {
        this.errors.date_of_birth = "";
      }
    },
    checkPasswordStrength() {
      const length = this.password.length;
      const hasUpperCase = /[A-Z]/.test(this.password);
      const hasNumber = /\d/.test(this.password);
      if (length >= 12 && hasUpperCase && hasNumber) {
        this.passwordStrengthText = "Strong";
        this.passwordStrengthColor = "green";
      } else if (length >= 8 && (hasUpperCase || hasNumber)) {
        this.passwordStrengthText = "Medium";
        this.passwordStrengthColor = "orange";
      } else {
        this.passwordStrengthText = "Weak";
        this.passwordStrengthColor = "red";
      }
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.idCardFile = file;
        this.errors.idCard = ""; // Clear any previous error
      } else {
        this.errors.idCard = "ID card is required.";
      }
    },
    async submitForm() {
      if (!this.isFormValid) {
        alert("Please fill out the form correctly.");
        return;
      }

      // Prepare form data for API call
      const formData = new FormData();
      formData.append("full_name", this.fullName);
      formData.append("email", this.email);
      formData.append("cine", this.cine);
      formData.append("date_of_birth", this.dateOfBirth);
      formData.append("place_of_birth", this.placeOfBirth);
      formData.append("id_card", this.idCardFile); // Ensure backend expects "id_card"
      formData.append("password", this.password);

      try {
        const response = await axios.post(
          "http://localhost:8000/api/signup/",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        alert(response.data.message); // Show success message
        this.$router.push("/signin"); // Redirect to sign-in page
      } catch (error) {
        console.error("Error during signup:", error.response); // Log de l'erreur
        if (error.response && error.response.data) {
          this.errors = error.response.data.errors || {};
          alert(error.response.data.error || "An error occurred during sign up.");
        } else {
          alert("An error occurred during sign up.");
        }
      }
    },
  },
};
</script>

<style scoped>

/* Navbar */
.navbar {
  background-color: #ffffff;
  padding: 10px 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.navbar-logo {
  height: 50px;
}
.navbar-brand span {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

/* Form Container */
.auth-form-container {
  margin-top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 100px);
  background-color: #f8f9fa;
}
.auth-form {
  width: 500px;
  padding: 30px;
  border-radius: 10px;
  background: #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
.auth-form h2 {
  text-align: center;
  color: #333;
  font-size: 1.8rem;
  margin-bottom: 20px;
}

/* Form Fields */
.form-group {
  margin-bottom: 15px;
}
.form-group label {
  font-weight: bold;
  display: block;
  margin-bottom: 8px;
}
.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
}
.form-group input:focus {
  border-color: #007bff;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.3);
}

/* Button */
button {
  width: 100%;
  padding: 10px;
  background-color: #0066cc;
  border: none;
  border-radius: 5px;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}
button:hover {
  background-color: #0056b3;
}
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Error Messages */
.error {
  color: red;
  font-size: 0.85rem;
}
</style>
