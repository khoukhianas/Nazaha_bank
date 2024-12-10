import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/Home.vue";
import AdminDashboard from "../views/AdminDashboard.vue";
import ValidationInscriptions from "../components/ValidationInscriptions.vue";
import DashboardPage from "../components/Dashboard.vue";
import AdminAccounts from "../components/Accounts.vue"; // Correct import
import AdminTransactions from "../components/Transactions.vue"; // Correct import
import AdminSupport from "../components/Support.vue"; // Correct import
import AdminSettings from "../components/Settings.vue"; // Correct import
// User Dashboard
import UserDashboard from "../views/UserDashboard.vue"; // Ajouté
import UserAccounts from "../components/UserAccounts.vue"; // Ajouté
import UserTransfer from "../components/UserTransfer.vue"; // Ajouté
import UserExternalTransfer from "../components/UserExternalTransfer.vue"; // Ajouté
import UserOnlinePayment from "../components/UserOnlinePayment.vue"; // Ajouté
import UserHistory from "../components/UserHistory.vue";
import SignUp from "../components/SignUp.vue";
import SignIn from "../components/SignIn.vue";


const routes = [
  { path: "/signup", component: SignUp },
  { path: "/signin", component: SignIn },
  // Accueil
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },

  // Routes pour l'administrateur
  {
    path: "/admin",
    component: AdminDashboard,
    children: [
      {
        path: "dashboard",
        name: "DashboardPage",
        component: DashboardPage,
      },
      {
        path: "validation",
        name: "ValidationInscriptions",
        component: ValidationInscriptions,
      },
      {
        path: "accounts",
        name: "AdminAccounts",
        component: AdminAccounts,
      },
      {
        path: "transactions",
        name: "AdminTransactions",
        component: AdminTransactions,
      },
      {
        path: "support",
        name: "AdminSupport",
        component: AdminSupport,
      },
      {
        path: "settings",
        name: "AdminSettings",
        component: AdminSettings,
      },
    ],
  },

  // Routes pour l'utilisateur
  {
    path: "/user",
    component: UserDashboard,
    children: [
      {
        path: "accounts",
        name: "UserAccounts",
        component: UserAccounts,
      },
      {
        path: "transfer",
        name: "UserTransfer",
        component: UserTransfer,
      },
      {
        path: "external-transfer",
        name: "UserExternalTransfer",
        component: UserExternalTransfer,
      },
      {
        path: "online-payment",
        name: "UserOnlinePayment",
        component: UserOnlinePayment,
      },
      {
        path: "history",
        name: "UserHistory",
        component: UserHistory,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
