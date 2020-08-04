import logging
logging.basicConfig(level=logging.INFO,file = "text.log",
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

a = 5
b = 11

if a > b:
    logging.info("Yes i am there")
elif a < b:
    logging.info("Yahooo!!")
else:
    logging.debug("ffhafj")

