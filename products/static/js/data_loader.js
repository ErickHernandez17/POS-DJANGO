var contenedor = document.getElementById('tbody');
const list_elements = async() => {
    try{
        const response = await fetch("./get-products");
        const data = await response.json();
        
        if (data.message == "Success"){
            var opciones = ``;
            data.products.forEach((product)=>{
                opciones+=`<tr>
                    <td>${product.product}</td>
                    <td>${product.price}</td>
                    <td>${product.category}</td>
                    <td>
                        <a class="btn btn-primary btn-sm open-popup" data-update-url="/product/update/${product.id}">Editar</a>
                    </td>
                    <td>
                        <a class="btn btn-danger btn-sm delete-item" data-product-id="${product.id}">Eliminar</a>
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
        console.log('ventana abierta');
      popup.updateUrl = $(this).data("update-url");
    });
  
    // Escuchar el evento de mensaje desde la ventana emergente
    window.addEventListener('message', function(event) {
      if (event.data.action === 'popupClosed' && event.data.message === 'Success') {
        // Actualizar la lista de categorías
        console.log('Se cerró la ventana de edición');
        list_elements();
      }
    });
  });
  
  
  $(document).ready(function() {
    // Delegación de eventos para los botones de "Eliminar"
    $(document).on("click", ".delete-item", function(event) {
        event.preventDefault();
        var productId = $(this).data("product-id");
        
        // Mostrar ventana emergente de confirmación
        var confirmDelete = confirm("¿Estás seguro de que deseas eliminar esta producto?");
        
        if (confirmDelete) {
            // Realizar la eliminación
            deleteCategory(productId);
        }
    });

});

function deleteCategory(productId) {
    $.ajax({
        url: `/product/delete/${productId}/`,  // Cambia la URL según tu configuración
        type: "POST",
        data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Agrega el token CSRF
        success: function(data) {
            if (data.message === "success") {
                // Actualizar la lista de categorías
                list_elements();
            } else {
                console.log('hola');
                alert("Error al eliminar el producto");
            }
        }
    });
}