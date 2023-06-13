/*Pipeline*/


[
  {
    $lookup:
      /*Linkando as duas tabelas utilizando o campo Montadora*/
      {
        from: "Montadoras",
        localField: "Montadora",
        foreignField: "Montadora",
        as: "Info_montadora"
      },
  },
  {
    $unwind: "$Info_montadora" /*Abrindo o campo montadoras para ter acessos aos dados*/
  },
  {
    $group: {
      /*Categorizando os carros com base no Pais*/
      _id: "$Info_montadora.Pais",
      Carro: {
        $push: "$Carro"
      }
    }
  }
]