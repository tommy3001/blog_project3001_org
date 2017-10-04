.. _introfabric:


****************************************************
-Python Packages- Part 10: Fabric
****************************************************

"Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks."

With `fabric <http://www.fabfile.org/>`_ you are able to automate your server maintenance, e.g. run the the same tasks on different servers.

Fabris is used to automate the usage of ssh during server administration tasks.

What I want to do is some alien observation with network cams.

For example, you are the admin of some different space stations with its own local IP-areas and the videos should be saved on the local space (the bandwidth to the Mars is very expensive).
What you now need is the possibility to manage the records on the stations from your couch through a save connection. Every cam has its own IP in the local network area of the space station.
I decided that VLC is a good tool to record the streams.

.. code-block:: python
    :linenos:

    import time
    import  fabric.api as fbc
    fbc.env.password = '123456' #Secret Password
    fbc.env.hosts = [
        'master@MarsStation.univ',
        'master@VenusStation.univ',
        'master@PlutoStation.univ',

    ]

    hours=1
    videoLength=  hours*3600
    RecordStartTime =0
    CamIPs=[]

    #Cam IPs are for each Cam ona the Space Station the same
    CamIPs.append( "192.168.0.101")
    CamIPs.append( "192.168.0.102")
    CamIPs.append( "192.168.0.103")

    TimeNow = 3600*time.localtime()[3]+60*time.localtime()[4]+time.localtime()[5]
    def record():
        for indx, IP in enumerate(IPs):
            #Todo: set the command line version of vlc
            fbc.run("vlc http://" + IP +"/mjpg/video.mjpg --run-time=" + str(videoLength)+ " --sout=\"#std{access=file,dst='/Video/"+str(TimeNow)+"_"+str(indx)+".mp4'}\" vlc://quit")
    def getRecord():
        for indx, IP in enumerate(IPs):
            fbc.get("/Video/"+str(TimeNow)+"_"+str(indx)+".mp4")

    recordingStarted= False
    while True:
        if  not recordingStarted:
            RecordStartTime=TimeNow
            recordingStarted = True
            fbc.execute(record, hosts=fbc.env.hosts)
        elif (RecordStartTime + videoLength)<TimeNow:
            recordingStarted = False
            fbc.execute(getRecord, hosts=fbc.env.hosts)
        TimeNow = 3600*time.localtime()[3]+60*time.localtime()[4]+time.localtime()[5]
        time.sleep(1)

fbc.env.password is our ssh password, and fbc.env.hosts are our video server on the space stations.
Here we have 2 function definitions, record() and getrecord(). The function record() starts the recording of the individual cam by its local ip.
The function getRecord() download the videos from the remote machine. The function call fbc.execute(record, hosts=fbc.env.hosts)
executes the function record() locally on each mashine  in the hosts list. The same behaviour is done with bc.execute(getRecord, hosts=fbc.env.hosts).
fbc.run() in record() calls a program on the host and fbc.get() in getRecord() is able to copy files to the the machine from where you execute the script.
