/*Pipeline*/


[
  {
    $lookup:
      /**
       * from: The target collection.
       * localField: The local join field.
       * foreignField: The target join field.
       * as: The name for the results.
       * pipeline: Optional pipeline to run on the foreign collection.
       * let: Optional variables to use in the pipeline field stages.
       */
      {
        from: "Montadoras",
        localField: "Montadora",
        foreignField: "Montadora",
        as: "Info_montadora"
      },
  },
  {
    $unwind: "$Info_montadora"
  },
  {
    $group: {
      _id: "$Info_montadora.Pais",
      Carro: {
        $push: "$Carro"
      }
    }
  }
]