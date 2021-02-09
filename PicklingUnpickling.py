import pickle


def pickle_data():
    data = {
        'Name': 'Yogesh',
        'Age': 32,
        'Address': 'Mandwada',
        'Country': 'India'
    }
    filename = 'PersonalInfo'
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()


pickle_data()


def unpickle_data():
    filename = 'PersonalInfo'
    file = open(filename, 'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data


print(unpickle_data())
