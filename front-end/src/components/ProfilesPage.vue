<script>
import RoommiesView from './RoommiesComponent.vue'
import axios from 'axios'
export default {
    components: {
        RoommiesView
    },
    data (){
        return{
            users: [],
        }
    },
    created() {
        if(localStorage.getItem("user_nombre")){
            if(localStorage.getItem("usuarios") != null){
                this.users = JSON.parse(localStorage.getItem("usuarios"));
            } else{
                this.fetchUsers();
            }
        }else{
            this.$router.push('/login');
        }
    },
    methods: {
        fetchUsers: async function() {
            const res = await fetch('http://127.0.0.1:5000/users_dist/'+localStorage.getItem("set_distrito"));
            const data = await res.json();
            this.users = data;
            this.updateLocalStorage();
        },
        updateLocalStorage: function(){
            localStorage.setItem("usuarios",JSON.stringify(this.users));
        }

    }
}
</script>

<template>
    <header class="text-center">
        <h1></h1>
        <h3 class="name">Encuentra tu <strong>Roommie</strong></h3>
    </header>
    <RoommiesView v-for="user in users"
        :nombre="user.nombre"
        :apellido="user.apellido"
        :email="user.email"
        :edad="user.edad"
        :descripcion="user.descripcion"
        :distrito="user.distrito"
    ></RoommiesView>



</template>