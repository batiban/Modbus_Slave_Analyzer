from streamlit.web import bootstrap


real_script = 'main.py'


bootstrap.run(real_script, f'streamlit run.py {real_script}', [], {})