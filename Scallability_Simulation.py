# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

import itertools

print("Modules imported successfully.")


# Effort calculation functions (Lines of Code, based on the interaction, node type and setup)
def calculate_a(node_datamodel_lines, node_num_of_communities, community_datamodel_average_lines, num_of_policies, policy_datamodel_average_line, node_num_of_data_models, api_call_cost, data_model_datamodel_average_lines):
    return (node_datamodel_lines + node_num_of_communities * community_datamodel_average_lines + num_of_policies * policy_datamodel_average_line + node_num_of_data_models *data_model_datamodel_average_lines) + api_call_cost * (1 + node_num_of_communities + num_of_policies + node_num_of_data_models)

def calculate_b(data_discovery_lines, interaction_creation_lines):
    return data_discovery_lines + interaction_creation_lines

def calculate_c(protocol_converter_lines, data_model_converter_lines):
    return protocol_converter_lines + data_model_converter_lines

def calculate_d(lines_of_code_for_initiated_collaboration_and_policy_exchange):
    return lines_of_code_for_initiated_collaboration_and_policy_exchange

# Generate nodes with semi-random properties, LoC here are taken from the experimental scenarios
def generate_nodes(num_nodes, percentage_preconfigured, percentage_types):
    num_types = round(num_nodes * percentage_types / 100)
    if (num_types==0):
        num_types=1
    types = [f'type_{i}' for i in range(num_types)]
    nodes = []
    for i in range(num_nodes):
        type_index = i % num_types  # Round-robin assignment of types
        state = 'preconfigured' if random.random() < percentage_preconfigured / 100 else 'clean'
        nodes.append({
            'id': i,
            'state': state,
            'node_datamodel_lines': random.randint(40,50),  
            'num_of_communities': random.randint(1, 10), 
            'community_datamodel_average_lines': random.randint(30, 40),
            'data_model_datamodel_average_lines': random.randint(40, 60),
            'num_of_policies': random.randint(0, 3),  
            'policy_datamodel_average_line': random.randint(10, 40),  
            'node_num_of_data_models': random.randint(1, 4),  
            'api_call_cost': random.randint(1, 3),  
            'data_discovery_lines': random.randint(14,20),  
            'interaction_creation_lines': random.randint(20,22),  
            'protocol_converter_lines': random.randint(75,90),  
            'data_model_converter_lines': random.randint(534,600),  
            'lines_of_code_for_initiated_collaboration_and_policy_exchange': random.randint(10, 20),
            'type': types[type_index],
            'marked_interactions': []
            
        })
    print(f"{len(nodes)} nodes generated successfully.")
    
    return nodes

def generate_edges_based_on_node_percentage(nodes, context_exchange_percentage, data_exchange_percentage):
    total_nodes = len(nodes)
    num_nodes_for_context_exchange = int(total_nodes * context_exchange_percentage / 100)
    num_nodes_for_data_exchange = int(total_nodes * data_exchange_percentage / 100)

    # Randomly selecting nodes for context and data exchanges
    nodes_for_context_exchange = random.sample(nodes, num_nodes_for_context_exchange)
    nodes_for_data_exchange = random.sample(nodes, num_nodes_for_data_exchange)

    # Generating edges among the selected nodes
    context_exchange_edges = list(itertools.combinations([node['id'] for node in nodes_for_context_exchange], 2))
    data_exchange_edges = list(itertools.combinations([node['id'] for node in nodes_for_data_exchange], 2))

    edges = []
    for edge in context_exchange_edges:
        edges.append((edge[0], edge[1], 'context_exchange'))
    for edge in data_exchange_edges:
        edges.append((edge[0], edge[1], 'data_exchange'))
        
    print(f"{len(edges)} edges generated based on node percentage.")
    return edges


def find_networks(nodes, edges):
    def dfs(node_id, visited, current_net):
        visited.add(node_id)
        current_net.add(node_id)
        for edge in edges:
            if edge[2] == 'context_exchange' and (edge[0] == node_id or edge[1] == node_id):
                neighbour_id = edge[1] if edge[0] == node_id else edge[0]
                if neighbour_id not in visited:
                    dfs(neighbour_id, visited, current_net)

    visited = set()
    networks = []
    for node in nodes:
        if node['id'] not in visited:
            current_net = set()
            dfs(node['id'], visited, current_net)
            networks.append(current_net)
    return networks



# Calculate total effort for a scenario
def calculate_effort_for_scenario(nodes, edges):
    print("Starting effort calculation for the current scenario...")
    total_effort = 0
    networks = find_networks(nodes, edges)
    calculated_node_type_pairs = set()
    data_exchange_count = 0
    calculated_exchanges = set()
    small_count=0
    num_nodes=len(nodes)
    print(f"Calculating effort for {num_nodes} nodes...")
    for node in nodes:
        print(node['id'])
        node_network = next((net for net in networks if node['id'] in net), set())
        for edge in edges:
            if edge[0] == node['id']:  # Edge starts from this node
                target_node = next(n for n in nodes if n['id'] == edge[1])
                edge_type = edge[2]
                effort=0
                
                # Effort calculation logic (same as before)
                if edge_type == 'data_exchange':     
                    if node['state'] == 'clean':
                        node['state'] = 'preconfigured'  # Transition to preconfigured after first data exchange
                        effort = calculate_a(node['node_datamodel_lines'], node['num_of_communities'], node['community_datamodel_average_lines'], node['num_of_policies'], node['policy_datamodel_average_line'], node['node_num_of_data_models'], node['api_call_cost'],node['data_model_datamodel_average_lines'])
                        #print("I enter here I am clean")
                    #else:
                        #print("I dont enter here I am preconfiggured")
                    
                    effort += calculate_b(node['data_discovery_lines'], node['interaction_creation_lines'])
                    
                    node_type_pair = (node['id'], target_node['type'])
                    
                    exchange_key = (node['type'], target_node['type'])
                       # Check if this specific node-target type exchange is new in the network
                    if node_type_pair not in calculated_exchanges and (node['type'] !=target_node['type']):
                        network_marked = any((node['type'], target_node['type']) in other_node['marked_interactions'] or (target_node['type'], node['type']) in other_node['marked_interactions'] for other_node in nodes if other_node['id'] in node_network)
                        
                        if not network_marked:
                            effort += calculate_c(node['protocol_converter_lines'], node['data_model_converter_lines'])
                            calculated_exchanges.add(node_type_pair)
                            for other_node in nodes:
                                if other_node['id'] in node_network:
                                    other_node['marked_interactions'].append((node['type'], target_node['type']))                  
                elif edge_type == 'context_exchange':
                    effort = calculate_d(node['lines_of_code_for_initiated_collaboration_and_policy_exchange'])
                total_effort += effort
                data_exchange_count+=1             
    return total_effort, data_exchange_count

# Adjust the state of nodes to be preconfigured or clean based on the percentage
def adjust_node_states(nodes, percentage_preconfigured):
    preconfigured_count = int(percentage_preconfigured / 100.0 * len(nodes))
    for node in nodes[:preconfigured_count]:
        node['state'] = 'preconfigured'
    for node in nodes[preconfigured_count:]:
        node['state'] = 'clean'
    return nodes
  
# Adjust the state of nodes to be preconfigured or clean based on the percentage
def adjust_node_types(nodes, percentage_types):
    num_nodes = len(nodes)
    num_types = round(num_nodes * percentage_types / 100)  # Calculate number of types based on percentage
    types = [f'type_{i}' for i in range(max(1, num_types))]  # Ensure at least one type

    for i, node in enumerate(nodes):
        type_index = i % len(types)
        node['type'] = types[type_index]

    return nodes

def adjust_node_marks(nodes):
    for i, node in enumerate(nodes):
        node["marked_interactions"]=[]
    return nodes


global_min_effort, global_max_effort = float('inf'), float('-inf')  

def simulate_scenarios(max_nodes, step, preconfigured_percentages, context_exchange_percentages, node_types_numbers):
    all_nodes = generate_nodes(max_nodes, 100, max(node_types_numbers))

    # Initialize arrays to store global min and max values for efforts
    global global_min_effort 
    global global_max_effort 
    # First pass to determine global min and max efforts
    for node_type_num in node_types_numbers:
        for preconfigured_percentage in preconfigured_percentages:
            for context_exchange_percentage in context_exchange_percentages:
                efforts = []

                for num_nodes in range(step, max_nodes + 1, step):
                    nodes_subset = all_nodes[:num_nodes]
                    node_subset = adjust_node_states(nodes_subset, preconfigured_percentage)
                    node_subset = adjust_node_marks(nodes_subset)
                    adjust_node_types(nodes_subset, node_type_num)
                    
                    edges = generate_edges_based_on_node_percentage(nodes_subset, context_exchange_percentage, 100)
                    total_effort, _ = calculate_effort_for_scenario(nodes_subset, edges)
                    efforts.append(total_effort)

                # Update global min and max
                global_min_effort = min(global_min_effort, min(efforts))
                global_max_effort = max(global_max_effort, max(efforts))

    # Initialize a multi-panel plot
    fig, axs = plt.subplots(len(node_types_numbers), len(preconfigured_percentages) * len(context_exchange_percentages), figsize=(15, 10))

    # Second pass to plot using the global effort limits
    for i, node_type_num in enumerate(node_types_numbers):
        for k, preconfigured_percentage in enumerate(preconfigured_percentages):
            for j, context_exchange_percentage in enumerate(context_exchange_percentages):
                efforts = []
                exchanges = []

                for num_nodes in range(step, max_nodes + 1, step):
                    nodes_subset = all_nodes[:num_nodes]
                    node_subset = adjust_node_states(nodes_subset, preconfigured_percentage)
                    node_subset = adjust_node_marks(nodes_subset)
                    adjust_node_types(nodes_subset, node_type_num)
                    edges = generate_edges_based_on_node_percentage(nodes_subset, context_exchange_percentage, 100)
                    total_effort, ex = calculate_effort_for_scenario(nodes_subset, edges)
                    exchanges.append(ex)
                    efforts.append(total_effort)

                # Plot on the appropriate subplot
                ax = axs[i, k * len(context_exchange_percentages) + j]
                line, = ax.plot(range(step, max_nodes + 1, step), efforts, marker='o')

                # Add annotations for exchanges
                for x, y, exchange in zip(range(step, max_nodes + 1, step), efforts, exchanges):
                    ax.annotate(str(exchange), (x, y), textcoords="offset points", xytext=(0,10), ha='center')

                ax.set_ylim(global_min_effort, global_max_effort)
                ax.set_title(f'DT%: {node_type_num},CE: {context_exchange_percentage}%, PC: {preconfigured_percentage}%')
                ax.grid(True)

    # Set common labels and a legend
    for ax in axs.flat:
        ax.set(xlabel='Nodes - Federations', ylabel='Total Effort (LoC)')
    plt.legend(loc='upper center', bbox_to_anchor=(-0.1, -0.1), ncol=len(context_exchange_percentages))
    plt.tight_layout()
    plt.show()

# Run the simulation
#Note the entire simulation takes a long time to run, in order to see a faster example 
#you can reduce the number of nodes present in the network (e.g from 100 to 50) and only run one configuration instead of the three below.
#e.g simulate_scenarios(50, 10, [50], [0, 50,100],[0,50,100])            
#simulate_scenarios(50, 10, [50], [0, 50,100],[0,50,100]) 
#You can also play with the configuration percentages to have more the the middleground (50%) and the extremes (0%,100%) for CE%,PC% and DT%
#See CCduit paper for detailed explanations of each variable

simulate_scenarios(100, 10, [0], [0, 50,100],[0,50,100])
print("1st done")
simulate_scenarios(100, 10, [50], [0, 50,100],[0,50,100])
print("2nd done")
simulate_scenarios(100, 10, [100], [0, 50,100],[0,50,100])
print("3rd done")




