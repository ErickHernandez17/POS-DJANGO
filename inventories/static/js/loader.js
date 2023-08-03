var contenedor = document.getElementById('tbody');
const list_elements = async() => {
    try{
        const response = await fetch("./inventories");
        const data = await response.json();
        if (data.message == "Success"){
            var opciones = ``;
            data.inventories.forEach((inventory)=>{
                opciones+=`<tr>
                    <td>${inventory.product__product}</td>
                    <td>${inventory.quantity}</td>
                    <td>${inventory.product__price}</td>
                    <td>${ inventory.create_date}</td>
                    <td>
                        <a class="btn btn-primary btn-sm open-popup" data-update-url="/inventory/update/${inventory.id}">Editar</a>
                    </td>
                    <td>
                        <a class="btn btn-danger btn-sm">Eliminar</a>
                    </td>
                </tr>`;
            });
            contenedor.innerHTML = opciones;
        }else{
            alert("Error al obtener las categorias")
        }

    }catch(error){
        console.log(error);
    }
}


const cargaInicial = async() => {
    await list_elements();
}


window.addEventListener("load", async() =>{
    await cargaInicial();
});

$(document).ready(function() {
    // Delegación de eventos para los botones de "Editar"
    $(document).on("click", ".open-popup", function(event) {
      event.preventDefault();
      var url = $(this).data("update-url");
      var popup = window.open(url, "Editar Producto", "width=800,height=600");
      popup.updateUrl = $(this).data("update-url");
    });
  
    // Escuchar el evento de mensaje desde la ventana emergente
    window.addEventListener('message', function(event) {
      if (event.data.action === 'popupClosed' && event.data.message === 'Success') {
        // Actualizar la lista de categorías
        list_elements();
      }
    });
  });
  
  
  