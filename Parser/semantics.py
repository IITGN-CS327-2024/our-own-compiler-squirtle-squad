import pickle
import node_classes
import rich
# from Parser import node_classes
# Specify the path to the pickle file
pickle_file_path = '/home/sachin/Desktop/our-own-compiler-squirtle-squad/graph.pkl'

# Load the AST from the pickle file
with open(pickle_file_path, 'rb') as file:
    ast = pickle.load(file)
rich.print(ast)
ast.render('tree',format='png', view=True)
