import typer
from rich import print
from rich.table import Table
from gptprompts import GptGenerationTopic



def main():
	print("[bold red]Bienvenido a este asistente con IA [/bold red]")

	topic = typer.prompt("\nPor favor escribe el tema del que quieres hablar ")

	gpt_topic = GptGenerationTopic(topic)

	while True:

		table = Table("Comando", "Descripción")
		table.add_row("1", "Opciones de Opcion multiple con respuesta")
		table.add_row("2", "Resumir puntos claves")
		table.add_row("3", "Tarjetas de Memorización")
		table.add_row("4", "Mapa mental")
		table.add_row("5", "Escribir nuevo tema")
		table.add_row("6", "Salir")


		print(table)

		command = typer.prompt("\nPor favor selecciona el comando en base a la tabla ")

		try:
			argument = int(command)
			getAnswer(argument, gpt_topic)
		except ValueError:
			print("[bold red]Comando inválido. Por favor selecciona un número del 1 al 6[/bold red]")
			continue
		
	#print(f"[bold green]> [/bold green] [green]{answer}[/green]")
		

def getAnswer(argument, gpt_topic):
    if argument == 1:   	
        print(gpt_topic.generateMultipleAnswerQuestions())
    elif argument == 2:
        print(gpt_topic.generateSummary())
    elif argument == 3:
        print(gpt_topic.generateFlashcards())
    elif argument == 4:
        print(gpt_topic.generateMindMap())
    elif argument == 5:
        main()  # restart the program
    elif argument == 6:
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego amigo!")
            raise typer.Abort()
    print("\n")


if __name__ == "__main__":
    typer.run(main)

#I want to add this code above the loading time