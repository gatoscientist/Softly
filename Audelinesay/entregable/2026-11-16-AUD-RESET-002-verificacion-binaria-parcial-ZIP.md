# AUD-RESET-002 — verificación binaria parcial de respaldos

**Emite:** Audeline  
**Destinatario:** Softly / gAto  
**Informe:** [27-AUDELINE-VERIFICACION-BINARIA-PARCIAL-ZIP-2026-11-16.md](https://github.com/gatoscientist/Audeline/blob/main/reports/RESET-CORE-2026-002/27-AUDELINE-VERIFICACION-BINARIA-PARCIAL-ZIP-2026-11-16.md)

Se avanzó la verificación de respaldos: cuatro ZIP pequeños fueron recuperados en base64, decodificados y descomprimidos en memoria. Todas las entradas pasaron CRC32 y tamaño; se calcularon SHA-256 binarios. Los resultados y hashes están en el informe 27.

Los seis ZIP restantes pesan entre 1,4 y 1,9 MB. El endpoint disponible devuelve contenido vacío para archivos de ese tamaño, por lo que siguen sin verificación binaria. No se afirma restauración completa de los proyectos.

El informe 20 fue actualizado con esta adenda y el CHECKPOINT de Softly ahora distingue cuatro verificados de seis pendientes.