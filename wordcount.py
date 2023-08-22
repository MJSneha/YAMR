from mapreduce import MapReduce
import sys

class WordCount(MapReduce):
    def __init__(self, input_dir, output_dir, n_mappers, n_reducers):
        MapReduce.__init__(self,  input_dir, output_dir, n_mappers, n_reducers)

    def mapper(self, key, value):
        """
        mapper for word_count
        """
        results = []
        default_count = 1
        for word in value.split():
            if self.is_valid_word(word):
                results.append((word.lower(), default_count))
        return results

    def is_valid_word(self, word):
        """
        word to check
        """
        return all(64 < ord(character) < 128 for character in word)

    def reducer(self, key, values):
        """Reducer for word_count
        """
        wordcount = sum(value for value in values)
        return key, wordcount


if __name__ == '__main__':
  if (len(sys.argv) != 4):
    print ("Please provide the following arguments: input directory, output directory, number of workers.")
    print ("Default arguments used: 'input_dir' 'output_dir' 4")
    import settings
    input_dir, output_dir, n_mappers, n_reducers = settings.default_input_dir, settings.default_output_dir, settings.default_n_mappers, settings.default_n_reducers
  else:
      input_dir = sys.argv[1]
      output_dir = sys.argv[2]
      n_mappers = int(sys.argv[3])
      n_reducers = int(sys.argv[3])
  word_count = WordCount(input_dir, output_dir, n_mappers, n_reducers)
  word_count.run()
  result = (word for word in word_count.join_outputs())

