library(dplyr)
library(readr)

#need to set working directory for the read to work (rootdir of the repo)
data <- read.csv("./../../Dataset/songdata.csv", stringsAsFactors = FALSE)

singer_texts <- data %>% filter(data$artist == "Rihanna")

texts <- data.frame(singer_texts$text)

write.table(texts, file = "./singer_lyrics/rihanna.txt", sep = ". ",
            row.names = FALSE, col.names = FALSE)



