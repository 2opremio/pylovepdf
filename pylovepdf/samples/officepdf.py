from pylovepdf.tools.officepdf import OfficeToPdf
import time

start = time.time()
t = OfficeToPdf('project_public_XXXXXXXXXXXXXXXXX', verify_ssl=True)
t.add_file('sample.docx')
t.debug = False
t.set_output_folder('/Users/fons/certus/ilovepdf/')

t.execute()
t.download()
end = time.time()
print("Time spent: %f ms" % ((end - start) * 1000) )
t.delete_current_task()
