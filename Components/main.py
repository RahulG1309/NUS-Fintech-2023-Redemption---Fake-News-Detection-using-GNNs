from json import load
import graph_creation
import load_model
import encoder

if __name__ == "__main__":
    # Intialize the graph cretaion object
    g = graph_creation.Graph()

    # Retrieve the news url to predit for
    news_url = input("Input new urls : ")

    # Get the graph of the news_url propogation in twitter
    G, news_data = g.get_graph_of_news_url(news_url)

    # Enocde the data using users last 200 tweets and profile features
    e = encoder.Encoder()   # initialize the encoder object
    inputToGNN = e.getInputToModel(G, news_data)
    print(type(inputToGNN))
    print(inputToGNN.shape)

    # Loading the torch GNN model
    model = load_model.load_model()

    # Processding the egde indices
    edge_index = load_model.get_processed_data(graph=G)
    print(edge_index)

    # Predicting the veracity of the news article
    prediction = load_model.predict_all(
        model=model, data=inputToGNN, edge_index=edge_index)

    # Return the prediction and propogation graph
    print(prediction)
