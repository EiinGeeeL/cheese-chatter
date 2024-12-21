few_shot_examples = [
    # Examples Summarization
    {
        "input": "¿Me podrías hacer un resumen de los últimos 25 mensajes?",
        "output": """
        - Mensajes: 25
        - Temas generales:
            - **Cultura y entretenimiento**:
                - 'Lucía': Recomendó un libro de ficción histórica.
                - 'David': Habló sobre una exposición de arte que visitó el fin de semana.
                - 'Marta': Compartió un enlace a una nueva serie de TV.
            - **Salud**:
                - 'Jorge': Mencionó una rutina de ejercicios para mejorar la postura.
                - 'Sofía': Habló sobre recetas saludables para desayunos rápidos.
        """
    },
    {
        "input": "Quiero un resumen de los últimos 50 mensajes.",
        "output": """
        - Mensajes: 50
        - Temas generales:
            - **Proyectos colaborativos**:
                - 'Andrés': Propuso un diseño inicial para el proyecto grupal.
                - 'Clara': Aportó ideas sobre la estructura del contenido.
                - 'Luis': Indicó que se encargará de la parte técnica.
            - **Deportes**:
                - 'Pedro': Comentó sobre el partido de fútbol de la semana pasada.
                - 'Juan': Sugirió organizar una partida de tenis el sábado.
            - **Cine**:
                - 'Carlos': Propuso ir al cine y recomendó una película de ciencia ficción.
        """
    },
    {
        "input": "¿Puedes hacer un resumen de las últimas 18 conversaciones?",
        "output": """
        - Mensajes: 18
        - Temas generales:
            - **Tecnología y novedades**:
                - 'Marta': Habló sobre las funciones del nuevo asistente de voz.
                - 'Elena': Preguntó sobre dispositivos compatibles con esa tecnología.
                - 'Miguel': Compartió un artículo sobre tendencias en inteligencia artificial.
            - **Social**:
                - 'Laura': Sugirió quedar para tomar algo este viernes.
                - 'David': Dijo que está disponible y propuso un lugar céntrico.
        """
    },
    # Examples ChitChat
    {
        "input": "¿Cuál es tu color favorito?",
        "output": "¡Me gustan todos los colores! Pero si tuviera que elegir, diría que el amarillo queso es bastante bonito. ¿Y el tuyo?"
    },
]