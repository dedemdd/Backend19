const btnComenzar = document.getElementById("btnComenzar");
const nombreEquipo = document.getElementById("nombreEquipo");
const imagenEquipo = document.getElementById("imagenEquipo");
const btnCrearEquipo = document.getElementById("btnCrearEquipo");

const BACKEND_URL = "http://127.0.0.1:3000";
btnComenzar?.addEventListener("click", (e) => {
  e.preventDefault();
  window.location.href = "crear-equipo.html";
});

// Cuando estemos en crear Equipo
if (window.location.pathname.includes("crear-equipo.html")) {
  let imagen;
  let imagenCreadaId;
  const generarUrlImagen = async () => {
    if (imagen) {
      const resultado = await fetch(`${BACKEND_URL}/generar-url`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          key: imagen.name.split(".")[0],
          path: "equipos",
          contentType: imagen.type,
          extension: imagen.name.split(".").slice(-1)[0], // La ultima posicion de un arreglo
        }),
      });

      return resultado.json();
    }
  };

  const subirAlBucket = async (url) => {
    const resultado = await fetch(url, { method: "PUT", body: imagen });
    console.log(resultado.status);
    return resultado.status === 200;
  };

  imagenEquipo.addEventListener("change", (e) => {
    imagen = imagenEquipo.files[0];
    console.log(imagenEquipo.files[0]);
    generarUrlImagen()
      .then((r) => {
        return subirAlBucket(r.content);
      })
      .then((status) => {
        if (!status) {
          console.error("Error al subir la imagen");
        }

        return fetch(`${BACKEND_URL}/imagen`, {
          body: JSON.stringify({
            key: imagen.name.split(".")[0],
            path: "equipos",
            contentType: imagen.type,
            extension: imagen.name.split(".").slice(-1)[0],
          }),
        });
      })
      .then((resultadoImagen) => {
        return resultadoImagen.json();
      })
      .then((imagenCreada) => {
        imagenCreadaId = imagenCreada.id;
      })
      .catch((e) => {
        console.log(e);
      });
  });

  btnCrearEquipo.addEventListener("click", (e) => {
    e.preventDefault();

    fetch(`${BACKEND_URL}/equipos`, {
      method: "POST",
      body: JSON.stringify({
        nombre: nombreEquipo.value,
        imagenId: imagenCreadaId,
      }),
    })
      .then((r) => {
        alert("EQUIPO CREADO EXITOSAMENTE");
      })
      .catch((e) => {
        alert("ERROR AL CREAR EL EQUIPO");
      });
  });
}