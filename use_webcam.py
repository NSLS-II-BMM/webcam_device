
from webcam_device import AxisWebcam

base = os.path.join('/nsls2', 'data', 'pdf', 'legacy','processed', 'xpdacq_data', 'user_data', 'webcam')
outboardcam = AxisWebcam(base=base, address='10.66.217.45', name='outboard webcam')
outboardcam.beamline_id = 'PDF (NSLS-II 28ID)'
outboardcam.annotation_string = 'Welcome to PDF'

downcam = AxisWebcam(root=root, address='10.66.217.46', name='downstream webcam')
downcam.beamline_id = 'PDF (NSLS-II 28ID)'
downcam.annotation_string = 'Welcome to PDF'
