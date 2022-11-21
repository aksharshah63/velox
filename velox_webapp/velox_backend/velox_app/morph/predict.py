
import utils

if __name__ == '__main__':
    from pprint import pprint
    predictor = 'predictor.dat'
    # input_dir = 'SteelBull.jpeg'
    input_file = '/home/zdenulo/2019Adaptation.jpg'
    ignore_list = None

    # res = utils.prediction_to_dict(predictor, input_file)
    # pprint(res)

    fd = open(input_file, 'rb')
    img_str = fd.read()
    fd.close()
    res2 = utils.prediction_from_bytes_to_dict(img_str)
    pprint(res2)
