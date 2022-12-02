<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
      <div class="col">
        <div class="card mb-4 rounded-3 shadow-sm">
          <div class="card-header py-3 bg-primary">
            <h4>1. REGÍSTRATE </h4>
          </div>
          <div class="card-body">
            <img src="../assets/img/macbook-profile-svgrepo-com.svg" alt="computer">
            <p class="card-text">
              Sé parte de una amplia red de personas que buscan a las personas adecuadas para compartir habitación.
            </p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-4 rounded-3 shadow-sm">
          <div class="card-header py-3 bg-primary">
            <h4>2. DESCUBRE </h4>
          </div>
          <div class="card-body">
            <img src="../assets/img/imac-incoming-message-svgrepo-com.svg" alt="computer">
            <p class="card-text">
              Visualiza todas las personas interesadas en encontrar Roomies y decide la persona que más se acerque a las características que buscas.
            </p>
          </div>
        </div>      </div>
      <div class="col">
        <div class="card mb-4 rounded-3 shadow-sm border-primary">
          <div class="card-header py-3 bg-primary">
            <h4>3. CONVIVE </h4>
          </div>
          <div class="card-body">
            <img src="../assets/img/dotting-people-svgrepo-com.svg" alt="computer">
            <p class="card-text">
              Prepárate para compartir nuevas experiencias con tu nuevo compañero en el tiempo que vivan juntos.
            </p>
          </div>
        </div>      </div>
    </div>
  </div>
</template>
<style scoped>
.container {
  margin-top: 10%;
}
.row {
    --bs-gutter-x: 1.5rem;
    --bs-gutter-y: 0;
    display: flex;
    flex-wrap: wrap;
    padding-right: calc(var(--bs-gutter-x) * .5);
    padding-left: calc(var(--bs-gutter-x) * .5);
    margin-right: auto;
    margin-left: auto;
}
/*resize img*/
img {
  width: 80%;
  height: 80%;
}


.card {
    --bs-card-spacer-y: 1rem;
    --bs-card-spacer-x: 1rem;
    --bs-card-title-spacer-y: 0.5rem;
    --bs-card-border-width: 1px;
    --bs-card-border-color: var(--bs-border-color-translucent);
    --bs-card-border-radius: 0.375rem;
    --bs-card-box-shadow: ;
    --bs-card-inner-border-radius: calc(0.375rem - 1px);
    --bs-card-cap-padding-y: 0.5rem;
    --bs-card-cap-padding-x: 1rem;
    --bs-card-cap-bg: rgba(0, 0, 0, 0.03);
    --bs-card-cap-color: ;
    --bs-card-height: ;
    --bs-card-color: ;
    --bs-card-bg: #fff;
    --bs-card-img-overlay-padding: 1rem;
    --bs-card-group-margin: 0.75rem;
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    height: var(--bs-card-height);
    word-wrap: break-word;
    background-color: var(--bs-card-bg);
    background-clip: border-box;
    border: var(--bs-card-border-width) solid var(--bs-card-border-color);
    border-radius: var(--bs-card-border-radius);
}

</style>