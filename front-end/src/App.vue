<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<script>
export default{
  components: {
    RouterLink,
    RouterView
  },
    data: function(){
        return {
            nombre: "",
            apellido: "",
            email: "",
            edad: "",
            mostrar: true
        }
    },
    mounted(){
        if(localStorage.getItem("user_nombre") != null){
          this.mostrar = false;
          this.nombre = localStorage.getItem("user_nombre");
          this.apellido = localStorage.getItem("user_apellido");
          this.email = localStorage.getItem("user_email");
          this.edad = localStorage.getItem("user_edad");
        }else{
          this.mostrar = true;
          this.nombre = "";
          this.apellido = "";
          this.email = "";
          this.edad = "";
        }
    },
    methods: {
      logout(){
        localStorage.clear();
        this.$router.push('/')
      }
  },
}
</script>

<template>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="src/assets/roommies.png" height="40" alt=""/>
      </a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link" aria-current="page">Inicio</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/search" class="nav-link" aria-current="page">Descubre</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/profiles" class="nav-link">Roommies</RouterLink>
          </li>
        </ul>
        <ul class="navbar-nav d-flex flex-row ms-auto me-3">
          <li class="nav-item">
            <RouterLink to="/register" class="nav-link" v-show="mostrar">Register</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/login" class="nav-link" v-show="mostrar">Login</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/Profile" class="nav-link capi" v-show="!mostrar">{{ nombre }} {{ apellido }}</RouterLink>
          </li>
          <li class="nav-item me-3 me-lg-0 dropdown" v-show="!mostrar">
            <a class="nav-link" href="/profile" id="navbarDropdown1" role="button" data-mdb-toggle="dropdown"
              aria-expanded="false">
              <img src="https://mdbootstrap.com/img/Photos/Avatars/img (31).jpg" class="rounded-circle" height="22"
                alt="" loading="lazy" />
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  
  <!-- Navbar -->
  <RouterView />
</template>

<style scoped>
.nav {
  background-color: #e3f2fd;
}
.nav-item {
  color: rgb(185, 149, 29);

}
.nav-bg{
  background-color: white;
}
.form-white.input-group>.form-control:focus {
  border-color: #fff;
  box-shadow: inset 0 0 0 1px #fff;
}

.navbar-dark .navbar-nav .nav-link {
  color: #fff;
}

.navbar-dark .navbar-nav .nav-link:hover,
.navbar-dark .navbar-nav .nav-link:focus {
  color: rgba(255, 255, 255, 0.75);
}

.capi{
  text-transform: capitalize;
}
</style>

