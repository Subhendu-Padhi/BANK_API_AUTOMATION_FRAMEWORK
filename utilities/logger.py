import logging

class LogGen:

    @staticmethod
    def loggen():

        logging.basicConfig(
            filename="logs/bank.log",
            format="%(asctime)s:%(levelname)s:%(message)s",
            level=logging.INFO
        )

        return logging.getLogger()