class BubbleSort:
    """
    Realiza o Bubble Sort.\n
      Parâmetros
        ----------\n
            lista : list
                Iterable que será usado para realizar o Bubble Sort
            
      Métodos
        ----------\n
            get()
                Retorna a lista ordenada
    """

    def __init__(self, lista: list):
        self.__lista = BubbleSort.__if_item_is(lista)
        self.__bubble_sort()
    
    
    @staticmethod
    def __if_item_is(item):
        if not isinstance(item, list):
            raise TypeError(f"Informado: '{type(item).__name__}' | Requisitado: 'list'")
        return item

    def get(self):
        return self.__lista


    def __trocar_posicao_pares(self, x, y):
        self.__lista[x], self.__lista[y] = self.__lista[y], self.__lista[x]


    def __bubble_sort(self):
        for i in range(len(self.__lista)):
            ordem_contraria = (len(self.__lista) - 1)
            for j in range(ordem_contraria, i, -1):
                if self.__lista[j] < self.__lista[j-1]:
                    self.__trocar_posicao_pares(j, j-1)



if __name__ == '__main__':
    lista = '[4,8,2,7,6,3,5,1,9,10]'

    BS = BubbleSort(lista)
    lista_organizada = BS.get()
