import subprocess

def user_input_team_size():
    """
    Prompt the user to input a valid team size and return it.
    """
    while True:
        input_value = input("Please input a team size: ")
        try:
            team_size = int(input_value)
            if team_size <= 0:
                print("Please enter a positive integer.")
                continue
            if team_size > 40:
                choice = input("Warning: Team size exceeds the recommended maximum of 40. Do you want to continue? (y/n): ")
                if choice.lower() != "y":
                    continue
            return team_size
        except ValueError:
            print("Please enter a valid integer.")

def fill_team_list(team_size):
    """
    Generate and return a list of team members based on the given team size.
    """
    return list(range(1, team_size+1))

def create_graph_file(filename, team_list):
    """
    Create a graph file with the given filename and team list.
    """
    with open(filename, 'w') as fp:
        fp.write('graph Brookslawvisualizer {\n')
        graph_entries = [f"{item} -- {item2}\n" for item in team_list for item2 in team_list if item < item2]
        fp.writelines(graph_entries)
        fp.write('}\n')

def execute_graphviz_command(gv_filename, output_filename):
    """
    Execute the GraphViz command to generate the graph file.
    """
    try:
        subprocess.run(["circo", "-V"], check=True)
        bash_command = f"circo -Tpng {gv_filename} -o {output_filename}"
        process = subprocess.run(bash_command.split(), stdout=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing GraphViz command: {e}")
        # Handle the error appropriately
    except FileNotFoundError:
        print("GraphViz (circo) is not installed. Please install GraphViz to generate the graph.")
        # Handle the error appropriately
    except Exception as e:
        print(f"An error occurred during graph generation: {e}")
        # Handle the error appropriately

# Usage:
team_size = user_input_team_size()
team_list = fill_team_list(team_size)
create_graph_file('brookslawvisualizer.gv', team_list)
execute_graphviz_command('brookslawvisualizer.gv', 'brookslawvisualizer.png')
