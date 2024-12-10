<template>
  <div class="admin-dashboard d-flex">
    <!-- Sidebar -->
    <nav class="sidebar bg-dark text-white vh-100">
      <div class="sidebar-header text-center py-4">
        <img
          src="https://via.placeholder.com/100"
          alt="Admin Avatar"
          class="rounded-circle mb-2"
          style="width: 80px; height: 80px;"
        />
        <h5>Admin {{ adminName }}</h5>
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
          <h5 class="m-0">Tableau de bord</h5>
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
        <h2 class="mb-4">Bienvenue, Admin {{ adminName }} !</h2>
        <!-- Router View (dynamic pages) -->
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminDashboard",
  data() {
    return {
      adminName: "Anas Bilal",
      searchQuery: "",
      isSidebarOpen: true,
      menuItems: [
        { text: "Dashboard", route: "/admin/dashboard", icon: "bi bi-speedometer" },
        { text: "Gestion des comptes", route: "/admin/accounts", icon: "bi bi-people" },
        { text: "Validation des inscriptions", route: "/admin/validation", icon: "bi bi-check-circle" },
        { text: "Transactions", route: "/admin/transactions", icon: "bi bi-cash-coin" },
        { text: "Support client", route: "/admin/support", icon: "bi bi-chat-dots" },
        { text: "Paramètres", route: "/admin/settings", icon: "bi bi-gear" },
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
.admin-dashboard {
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
