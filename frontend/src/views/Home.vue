<template>
  <div class="container-fluid">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-light">
      <a class="navbar-brand" href="#">
        <img src="\images\NB.png" alt="Logo" style="height: 50px;" />
        NazahaBank
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ml-auto">
          <!-- Menu déroulant pour les fonctionnalités -->
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="featuresDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Fonctionnalités
            </a>
            <div class="dropdown-menu" aria-labelledby="featuresDropdown">
              <a class="dropdown-item" href="#">Produits</a>
              <a class="dropdown-item" href="#">Services</a>
              <a class="dropdown-item" href="#">Support</a>
            </div>
          </li>
          <!-- Boutons Login et Register plus visibles -->
          <li class="nav-item">
            <router-link to="/signin" class="btn btn-outline-primary mx-2">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/signup" class="btn btn-primary">Register</router-link>          </li>
        </ul>
      </div>
    </nav>

    <!-- Hero Section avec arrière-plan image et animations -->
    <div class="hero-section">
      <div class="overlay"></div>
      <div class="hero-content text-center">
        <h1 class="display-4 animated fadeInDown">Bienvenue dans nazahaBank</h1>
        <p class="lead animated fadeInUp delay-1s">Votre banque, votre avenir.</p>
        <button class="btn btn-primary btn-lg mt-3 animated fadeInUp delay-2s">Découvrir Plus</button>
      </div>
    </div>

    <!-- Carousel avec transitions fluides et légendes améliorées -->
    <div id="mainCarousel" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#mainCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#mainCarousel" data-slide-to="1"></li>
        <li data-target="#mainCarousel" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <!-- Première diapositive -->
        <div class="carousel-item active">
          <img class="d-block w-100" src="\images\1920x600.png" alt="First slide" />
          <div class="carousel-caption d-none d-md-block">
            <img src="\images\fraudes.png" alt="Icon" class="mb-3" />
            <h5>Gestion des Comptes</h5>
            <p>Créez et gérez vos comptes facilement.</p>
          </div>
        </div>
        <!-- Deuxième diapositive -->
        <div class="carousel-item">
          <img class="d-block w-100" src="\images\1920x6001.png" alt="Second slide" />
          <div class="carousel-caption d-none d-md-block">
            <img src="\images\comptes.png" alt="Icon" class="mb-3" />
            <h5>Fraude Sécurisée</h5>
            <p>Protégez vos données avec nos outils avancés.</p>
          </div>
        </div>
        <!-- Troisième diapositive -->
        <div class="carousel-item">
          <img class="d-block w-100" src="\images\1920x6002.png" alt="Third slide" />
          <div class="carousel-caption d-none d-md-block">
            <img src="\images\transaction.png" alt="Icon" class="mb-3" />
            <h5>Transactions Rapides</h5>
            <p>Effectuez vos paiements en un clic.</p>
          </div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#mainCarousel" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Précédent</span>
      </a>
      <a class="carousel-control-next" href="#mainCarousel" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Suivant</span>
      </a>
    </div>

    <!-- Section des fonctionnalités avec cartes modernisées -->
    <div class="container mt-5 features-section">
      <div class="row text-center">
        <div class="col-md-4 mb-4">
          <div class="card feature-card h-100">
            <div class="card-body">
              <img src="https://via.placeholder.com/50" alt="Icon" class="mb-3" />
              <h5 class="card-title">Gestion des Comptes</h5>
              <p class="card-text">Créez, consultez et gérez vos comptes en toute simplicité.</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4">
          <div class="card feature-card h-100">
            <div class="card-body">
              <img src="https://via.placeholder.com/50" alt="Icon" class="mb-3" />
              <h5 class="card-title">Fraude Sécurisée</h5>
              <p class="card-text">Protégez vos données grâce à notre détection avancée.</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4">
          <div class="card feature-card h-100">
            <div class="card-body">
              <img src="https://via.placeholder.com/50" alt="Icon" class="mb-3" />
              <h5 class="card-title">Transactions Rapides</h5>
              <p class="card-text">Effectuez vos paiements en temps réel sans soucis.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer avec icônes de réseaux sociaux et formulaire d'abonnement -->
    <footer class="bg-dark text-white text-center py-4 mt-5">
      <div class="container">
        <div class="mb-3">
          <a href="#" class="text-white mx-2"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="text-white mx-2"><i class="fab fa-twitter"></i></a>
          <a href="#" class="text-white mx-2"><i class="fab fa-linkedin-in"></i></a>
          <a href="#" class="text-white mx-2"><i class="fab fa-instagram"></i></a>
        </div>
        <form class="form-inline justify-content-center mb-3">
          <div class="form-group">
            <label for="newsletterEmail" class="sr-only">Email</label>
            <input type="email" class="form-control mr-2" id="newsletterEmail" placeholder="Entrez votre email" />
          </div>
          <button type="submit" class="btn btn-primary">S'abonner</button>
        </form>
        <p>© 2024 NazahaBank. Tous droits réservés.</p>
        <p>
          <a href="#" class="text-white">Mentions légales</a> |
          <a href="#" class="text-white">Politique de confidentialité</a> |
          <a href="#" class="text-white">Contactez-nous</a>
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const navbar = document.querySelector(".navbar");
      if (window.scrollY > 50) {
        navbar.classList.add("navbar-scrolled");
      } else {
        navbar.classList.remove("navbar-scrolled");
      }
    },
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>


<style>
/* Styles globaux */
body {
  font-family: 'Roboto', sans-serif;
  color: #333;
}

/* Navbar */
.navbar {
  transition: background-color 0.3s ease;
}
.navbar-scrolled {
  background-color: rgba(255, 255, 255, 0.9) !important;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 100vh;
  background: url('~@/assets/accueill.png') center center/cover no-repeat;
}
.hero-section .overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 50, 0.5);
}
.hero-content {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  color: #fff;
}
.hero-content .btn {
  background-color: #0066cc;
  border: none;
}
.hero-content .btn:hover {
  background-color: #005bb5;
}

/* Carousel */
.carousel-item img {
  height: 600px;
  object-fit: cover;
}
.carousel-caption h5,
.carousel-caption p {
  animation-duration: 1s;
  animation-fill-mode: both;
}
.carousel-caption h5 {
  animation-name: fadeInDown;
}
.carousel-caption p {
  animation-name: fadeInUp;
}

/* Features */
.features-section .feature-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}
.features-section .feature-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

/* Footer */
footer a {
  transition: color 0.3s ease;
}
footer a:hover {
  color: #0066cc;
}
footer .form-control {
  border-radius: 0;
}
footer .btn {
  border-radius: 0;
  background-color: #0066cc;
  border: none;
}
footer .btn:hover {
  background-color: #005bb5;
}

/* Animations */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animated {
  animation-duration: 1s;
  animation-fill-mode: both;
}
.delay-1s {
  animation-delay: 1s;
}
.delay-2s {
  animation-delay: 2s;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-content {
    padding: 0 20px;
  }
}
</style>