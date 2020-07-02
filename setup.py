import cx_Freeze

executables = [cx_Freeze.Executable(script="gameshot.py", icon="data/Ball.ico")]

cx_Freeze.setup(
    name="Ball Shot Game",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["data"]
                           }}, executables=executables
)
