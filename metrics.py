import psutil
import sys


class Metrics:

    def get_data(self):
        represent_data = {
            "cpu": self.get_cpu,
            "mem": self.get_mem
        }
        return represent_data.get(sys.argv[1], self.not_valid_arg)()

    @staticmethod
    def get_mem():
        try:
            for key, value in dict(psutil.virtual_memory()._asdict()).items():
                print(f"{key.capitalize()}: {value},")
        except Exception as e:
            print(f"Ups, looks like we face an error while executing {sys.argv[1].upper()} command: \n  {e}")

    def get_cpu(self):
        try:
            for key, value in dict(psutil.cpu_times(percpu=False)._asdict()).items():
                print(f"{key.capitalize()}: {value},")
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
