<template>
   <div class="container-xl px-4 mt-4">
      <h3 class="text-down">
        <span class="margin-auto_content capi">
          Bienvenido {{ nombre }} {{ apellido }} 
          </span>
      </h3>
      <h3 class="text-down"><button class="boton" @click="logout">Cerrar sesión</button></h3>
    <hr class="mt-0 mb-4">
    <div class="row">
        <div class="col-xl-4">
            <!-- Profile picture card-->
            <div class="card mb-4 mb-xl-0">
                <div class="card-header">Foto de perfil</div>
                <div class="card-body text-center">
                    <!-- Profile picture image-->
                    <img class="img-account-profile rounded-circle mb-2" src="http://bootdey.com/img/Content/avatar/avatar1.png" alt="">
                    <!-- Profile picture help block-->
                    <div class="small font-italic text-muted mb-4">JPG or PNG no larger than 5 MB</div>
                    <!-- Profile picture upload button-->
                    <button class="btn btn-primary" type="button">Subir foto</button>
                </div>
            </div>
        </div>
        <div class="col-xl-8">
            <!-- Account details card-->
            <div class="card mb-4">
                <div class="card-header">Detalles de tu cuenta</div>
                <div class="card-body">
                    <form v-on:submit.prevent="add_descripcion">
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <label class="small mb-1" for="inputBirthday">Descripción</label>
                            </div>
                            <textarea class="form-control" aria-label="With textarea"  placeholder="Que es lo que mejor te describe" v-model="descripcion"></textarea>
                        </div>
                        <h1></h1>
                        <!-- Save changes button-->
                        <button class="btn btn-primary" type="submit">Añadir descripción</button>
                    </form>
                </div>
                <div class="card-body">
                    <label class="small mb-1" for="inputBirthday">Distrito de preferencia</label>
                    <div class="form-floating" >
            <select class="form-select " id="floatingSelect" aria-label="Floating label select example" >
                <option selected disabled>Escoge el distrito donde quisieras vivir</option> <option value="">ANCON</option>
                <option value="" >ATE</option> <option value="">BARRANCO</option> <option value="">BREÑA</option>
                <option value="">CARABAYLLO</option> <option value="">CHACLACAYO</option> <option value="">CHORRILLOS</option>
                <option value="">CIENEGUILLA</option> <option value="">COMAS</option> <option value="">EL AGUSTINO</option>
                <option value="">INDEPENDENCIA</option> <option value="">JESUS MARIA</option><option value="">LA MOLINA</option>
                <option value="">LA VICTORIA</option><option value="">LIMA</option><option value="">LINCE</option>
                <option value="">LOS OLIVOS</option><option value="">LURIGANCHO</option><option value="">LURIN</option>
                <option value="">MAGDALENA DEL MAR</option><option value="">MIRAFLORES</option><option value="">PACHACAMAC</option>
                <option value="">PUCUSANA</option><option value="">PUEBLO LIBRE</option><option value="">PUENTE PIEDRA</option>
                <option value="">PUNTA HERMOSA</option><option value="">PUNTA NEGRA</option><option value="">RIMAC</option>
                <option value="">SAN BARTOLO</option><option value="">SAN BORJA</option><option value="">SAN ISIDRO</option>
                <option value="">SAN JUAN DE LURIGANCHO</option><option value="">SAN JUAN DE MIRAFLORES</option>
                <option value="">SAN LUIS</option><option value="">SAN MARTIN DE PORRES</option><option value="">SAN MIGUEL</option>
                <option value="">SANTA ANITA</option><option value="">SANTA MARIA DEL MAR</option>
                <option value="">SANTA ROSA</option><option value="">SANTIAGO DE SURCO</option>
                <option value="">SURQUILLO</option><option value="">VILLA EL SALVADOR</option>
                <option value="">VILLA MARIA DEL TRIUNFO</option>
            </select>
            <h1></h1>
            <button class="btn btn-primary" type="submit" @click="add_distrito">Añadir distrito</button>
        </div>
                </div>
            </div>
        </div>
    </div>
</div>
  </template>
  
<script>
import axios from 'axios';

export default {
  name: 'Profile-Page',
  data() {
    return {
      nombre: '',
      apellido: '',
      email: '',
      edad: '',
      descripcion: "",
      distrito: "",
      monto: ""
    };
  },
  mounted(){
    if(localStorage.getItem('user_nombre')){
      this.nombre = localStorage.getItem('user_nombre');
      this.apellido = localStorage.getItem('user_apellido');
      this.email = localStorage.getItem('user_email');
      this.edad = localStorage.getItem('user_edad');
    }else{
      this.$router.push('/login');
    }
  },
  methods: {
      logout(){
        localStorage.clear();
        this.$router.push('/')
      },
      add_descripcion(){
        let json = {
            "descripcion": this.descripcion,
            "user_id": localStorage.getItem("user_id")
        };
        axios.post('http://127.0.0.1:5000/add_descripcion', json)
      },
      add_distrito(){
            var temp = this.distrito = document.getElementById("floatingSelect");
            this.distrito = temp.options[temp.selectedIndex].text;
            let json ={
                "distrito": this.distrito,
                "user_id": localStorage.getItem("user_id")
            }
            axios.post('http://127.0.0.1:5000/add_distrito', json)
      }
  },
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap');
.capi{
  text-transform: capitalize;
}

.boton{
  text-align: right;
}

body{margin-top:20px;
background-color:#f2f6fc;
color:#69707a;
}
.img-account-profile {
    height: 10rem;
}
.rounded-circle {
    border-radius: 50% !important;
}
.card {
    box-shadow: 0 0.15rem 1.75rem 0 rgb(33 40 50 / 15%);
}
.card .card-header {
    font-weight: 500;
}
.card-header:first-child {
    border-radius: 0.35rem 0.35rem 0 0;
}
.card-header {
    padding: 1rem 1.35rem;
    margin-bottom: 0;
    background-color: rgba(33, 40, 50, 0.03);
    border-bottom: 1px solid rgba(33, 40, 50, 0.125);
}
.form-control, .dataTable-input {
    display: block;
    width: 100%;
    padding: 0.875rem 1.125rem;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1;
    color: #69707a;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #c5ccd6;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border-radius: 0.35rem;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.nav-borders .nav-link.active {
    color: #0061f2;
    border-bottom-color: #0061f2;
}
.nav-borders .nav-link {
    color: #69707a;
    border-bottom-width: 0.125rem;
    border-bottom-style: solid;
    border-bottom-color: transparent;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    padding-left: 0;
    padding-right: 0;
    margin-left: 1rem;
    margin-right: 1rem;
}

.margin-auto {
  font-family: 'Fjalla One', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top:200px;
  
}
.text-down{
  font-family: 'Fjalla One', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top:5px;
        
}

.gradient-custom {
/* fallback for old browsers */
background: #eee709;
/* Chrome 10-25, Safari 5.1-6 */
background: -webkit-linear-gradient(to right, rgb(226, 219, 15), rgb(192, 221, 7));
/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
background: linear-gradient(to right, rgb(175, 203, 17), rgb(208, 255, 0))
}
</style>