import psutil
import sys


class Metrics:

    def __repr__(self):
        message = """
        This script is created to display metrics for cpu or mem: 
        
        @usage:
        pipenv run python metrics.py mem
        
        @params: 
        mem - to display memory metrics
        cpu - to display cpu metrics
        """
        print(message)
        return message

    def get_data(self):
        represent_data = {
            "cpu": self.get_cpu,
            "mem": self.get_mem,
            "help": self.__repr__
        }
        return represent_data.get(sys.argv[1].lower(), self.not_valid_arg)()

    @staticmethod
    def get_mem():
        try:
            for key, value in dict(psutil.virtual_memory()._asdict()).items():
                print(f"{key.capitalize()}: {value}")
            for key, value in dict(psutil.swap_memory()._asdict()).items():
                print(f"Swap {key.capitalize()}: {value}")
        except Exception as e:
            print(f"Ups, looks like we face an error while executing {sys.argv[1].upper()} command: \n  {e}")

    @staticmethod
    def get_cpu():
        try:
            for key, value in dict(psutil.cpu_times(percpu=False)._asdict()).items():
                print(f"{key.capitalize()}: {value}")
        except Exception as e:
            print(f"Ups, looks like we face an error while executing {sys.argv[1].upper()} command: \n  {e}")

    @staticmethod
    def not_valid_arg():
        message = f"""
        Parameter {sys.argv[1].upper()} is not valid. \n
        Please use:
        mem - to get memory metrics
        cpu - to get cpu metrics
        """
        print(message)


if __name__ == "__main__":
    metrics = Metrics()
    metrics.get_data()
