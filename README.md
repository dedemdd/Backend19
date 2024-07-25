# Repositorio de Backend de CodiGo G19
Bienvenido a mi repositorio, aqui podrás encontrar toda la información relacionado al curso.

Toda la información estará distribuida entre ramas en la cual cada semana sera 1 rama y tendremos el siguiente indice

1. [Semama 01]
2. [Semama 02]
3. [Semama 03]
4. [Semama 04]
5. [Semama 05]
6. [Semama 06]
7. [Semama 07]
8. [Semama 08]
9. [Semama 09]
10. [Semama 10]

11. copia de seguridad se realiza con el siguiten comando: pg_dump -U postgres -f copia_seguridad.sql finanzas
pg_dump -U postgres -F c -f copia_seguridad.backup finanzas

12. para restaurar la BD, no tiene que tener nada, y se aplica lo siguiente: psql -U postgres -d finanzas -v copia_seguridad.sql

13.para restaurar la BD con con pg_restore, se aplica lo siguiente: pg_restore -U postgres -d finanzas -v copia_seguridad.backup