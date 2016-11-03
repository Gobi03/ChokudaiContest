object Main extends App{
  val ar = Array.fill(1e5.toInt + 1)(true)

  ar(0) = false
  ar(1) = false

  var ind = 2
  while(ind * ind <= 1e9.toInt){
    if(ar(ind)){
      var i = 2
      while(ind * i <= 1e5.toInt){
        if(ar(ind * i))
          ar(ind * i) = false
        i += 1
      }
    }

    ind += 1
  }

  for(i <- 2 to ind){
    if(ar(i)){
      println(i)
    }
  }
}
