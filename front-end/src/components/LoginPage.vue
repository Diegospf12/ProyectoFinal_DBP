<script>
import axios from 'axios'
export default{
    name: 'Login',
    components: {

    },
    data: function(){
        return {
            email: "",
            password: "",
            error: "",
            error_msg: ""
        }
    },
    methods:{
        login(){
            let json = {
                "email" : this.email,
                "password": this.password
            };
            let config = {
                headers: {
                    "Content-Type": "application/json"
                }
            }
            axios.post('http://127.0.0.1:5000/get_user', json, config)
            .then(data =>{     
                if(data.data.email == this.email && data.data.password == this.password){
                    this.error = false;
                    this.error_msg = "correcto";
                    localStorage.setItem("user_id",data.data.id);
                    localStorage.setItem("user_nombre",data.data.nombre);
                    localStorage.setItem("user_apellido",data.data.apellido);
                    localStorage.setItem("user_email",data.data.email);
                    localStorage.setItem("user_edad",data.data.edad);
                    this.$router.push("/search");
                }else{
                    this.error = true;
                    this.error_msg = "Usuario o contraseña incorrecto";
                }
            })
        }
    }

}
</script>

<template>
    <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-dark text-white" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">

                <div class="mb-md-5 mt-md-4 pb-5">

                <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                <p class="text-white-50 mb-5">Ingresa tu email y contraseña!</p>
                
                <form v-on:submit.prevent="login" class="form-outline form-white mb-4">

                    <div class="form-outline form-white mb-4">
                        <input type="email" id="typeEmailX" class="form-control form-control-lg" placeholder="Email" v-model="email"/>
                    </div>
                    <div class="form-outline form-white mb-4">
                        <input type="password" id="typePasswordX" class="form-control form-control-lg" placeholder="Contraseña" v-model="password"/>
                    </div>
                    <p class="small mb-5 pb-lg-2"><a class="text-white-50" href="#!">Forgot password?</a></p>
                    <button class="btn btn-outline-light btn-lg px-5" type="submit">Login</button>
                </form>

                <div class="alert alert-danger" role="alert" v-if="error">
                    {{ error_msg }}
                </div>

                </div>

                <div>
                <p class="mb-0">Don't have an account? <a href="#!" class="text-white-50 fw-bold"><RouterLink to="/register" class="nav-link">Register</RouterLink></a>
                </p>
                </div>
            </div>
            
            </div>
        </div>
        </div>
    </div>
    </section>
</template>

<style scoped>
.gradient-custom {
/* fallback for old browsers */
background: #6a11cb;

/* Chrome 10-25, Safari 5.1-6 */
background: -webkit-linear-gradient(to right, rgba(106, 17, 203, 1), rgba(37, 117, 252, 1));

/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
background: linear-gradient(to right, rgba(106, 17, 203, 1), rgba(37, 117, 252, 1))
}
</style>