<script>
export default{
    name: "RoommiesView",
    props: ["nombre", "apellido","email","edad","distrito","carrera","descripcion"]
}
</script>

<template>
<div class="container bootstrap snippets bootdey">
<div class="panel-body inf-content">
    <div class="row">
        <div class="col-md-4">
            <img alt="" style="width:600px;" title="" class="img-circle img-thumbnail isTooltip" src="https://bootdey.com/img/Content/avatar/avatar7.png" data-original-title="Usuario"> 
            <ul title="Ratings" class="list-inline ratings text-center">
                <li class="capi">{{ nombre }}</li>
                <li class="capi">{{ apellido }}</li>
            </ul>
        </div>
        <div class="col-md-6">
            <div class="table-responsive">
            <table class="table table-user-information">
                <tbody>
                    <tr>    
                        <td>
                            <strong>
                                <span class="glyphicon glyphicon-user  text-primary"></span>    
                                Nombre:                                               
                            </strong>
                        </td>
                        <td class="text-color capi">
                            {{nombre}} 
                        </td>
                    </tr>
                    <tr>        
                        <td>
                            <strong>
                                <span class="glyphicon glyphicon-cloud text-primary"></span>  
                                Apellido:                                              
                            </strong>
                        </td>
                        <td class="text-color capi">
                            {{apellido}} 
                        </td>
                    </tr>
                    <tr>        
                        <td>
                            <strong>
                                <span class="glyphicon glyphicon-envelope text-primary"></span> 
                                Email                                                
                            </strong>
                        </td>
                        <td class="text-color">
                            {{email}} 
                        </td>
                    </tr>
                    <tr>        
                        <td>
                            <strong>
                                <span class="glyphicon glyphicon-envelope text-primary"></span> 
                                Edad:                                               
                            </strong>
                        </td>
                        <td class="text-color">
                            {{edad}} 
                        </td>
                    </tr>
                    <tr>        
                        <td>
                            <strong>
                                <span class="glyphicon glyphicon-envelope text-primary"></span> 
                                Distritos de preferencia:                                             
                            </strong>
                        </td>
                        <td class="text-color capi">
                            {{distrito}} 
                        </td>
                    </tr>
                    <tr>        
                        <td>
                            <strong>
                                <span class="glyphicon glyphicon-envelope text-primary"></span> 
                                Descripcion:                                             
                            </strong>
                        </td>
                        <td class="text-color">
                            {{descripcion}} 
                        </td>
                    </tr>                                   
                </tbody>
            </table>
            </div>
        </div>
    </div>
</div>
</div>
</template>

<style scoped>
 .inf-content{
    border:1px solid #DDDDDD;
    -webkit-border-radius:10px;
    -moz-border-radius:10px;
    border-radius:10px;
    box-shadow: 7px 7px 7px rgba(0, 0, 0, 0.3);
    margin: 30px;
}	

.text-color{
    color: darkcyan;
}

.capi{
    text-transform: capitalize;
}

</style>