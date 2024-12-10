<template>
    <div class="user-dashboard d-flex">
      <!-- Sidebar -->
      <nav class="sidebar bg-dark text-white vh-100">
        <div class="sidebar-header text-center py-4">
          <img
            src="https://via.placeholder.com/100"
            alt="User Avatar"
            class="rounded-circle mb-2"
            style="width: 80px; height: 80px;"
          />
          <h5>Bienvenue, {{ userName }}</h5>
        </div>
        <ul class="nav flex-column text-center">
          <li class="nav-item" v-for="item in menuItems" :key="item.text">
            <a
              class="nav-link text-white"
              :class="{ active: currentRoute === item.route }"
              :href="item.route"
            >
              <i :class="item.icon"></i> {{ item.text }}
            </a>
          </li>
          <li class="nav-item mt-auto">
            <a class="nav-link text-danger" href="#" @click="logout">
              <i class="bi bi-box-arrow-right"></i> Déconnexion
            </a>
          </li>
        </ul>
      </nav>
  
      <!-- Main Content -->
      <div class="main-content flex-grow-1">
        <!-- Header -->
        <nav class="navbar navbar-light bg-light shadow-sm px-3">
          <div class="d-flex align-items-center">
            <button class="btn btn-outline-primary me-3" @click="toggleSidebar">
              <i :class="isSidebarOpen ? 'bi bi-list' : 'bi bi-x-lg'"></i>
            </button>
            <h5 class="m-0">Tableau de bord utilisateur</h5>
          </div>
          <form class="d-flex">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Rechercher..."
              aria-label="Search"
              v-model="searchQuery"
            />
            <button class="btn btn-primary" type="button" @click="search">
              <i class="bi bi-search"></i>
            </button>
          </form>
        </nav>
  
        <!-- Dynamic Content -->
        <div class="container-fluid p-4">
          <h2 class="mb-4">Bienvenue, {{ userName }} !</h2>
          <!-- Router View (dynamic pages) -->
          <router-view></router-view>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserDashboard",
    data() {
      return {
        userName: "Utilisateur", // À remplacer par une donnée réelle
        searchQuery: "",
        isSidebarOpen: true,
        menuItems: [
          { text: "Mon Compte", route: "/user/account", icon: "bi bi-person-circle" },
          { text: "Virement", route: "/user/transfer", icon: "bi bi-arrow-left-right" },
          { text: "Transfert", route: "/user/external-transfer", icon: "bi bi-send" },
          { text: "Paiement en Ligne", route: "/user/online-payment", icon: "bi bi-credit-card" },
          { text: "Historique", route: "/user/history", icon: "bi bi-clock-history" },
        ],
      };
    },
    computed: {
      currentRoute() {
        return this.$route.path;
      },
    },
    methods: {
      toggleSidebar() {
        this.isSidebarOpen = !this.isSidebarOpen;
        document.querySelector(".sidebar").classList.toggle("d-none");
      },
      logout() {
        this.$router.push("/login");
      },
      search() {
        console.log("Rechercher :", this.searchQuery);
      },
    },
  };
  </script>
  
  <style scoped>
  .user-dashboard {
    height: 100vh;
  }
  
  .sidebar {
    width: 250px;
    transition: all 0.3s ease;
  }
  
  .sidebar .nav-link {
    padding: 10px 15px;
    transition: background-color 0.3s ease;
  }
  
  .sidebar .nav-link:hover {
    background-color: #495057;
    border-radius: 5px;
  }
  
  .sidebar .nav-link.active {
    background-color: #007bff;
    color: white !important;
    border-radius: 5px;
  }
  
  .main-content {
    overflow-y: auto;
  }
  
  .navbar {
    position: sticky;
    top: 0;
    z-index: 1000;
  }
  
  .container-fluid {
    margin-top: 20px;
  }
  </style>
  