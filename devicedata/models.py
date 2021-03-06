from django.db import models
import uuid

class Device(models.Model):
    """
    Model representing slave device.
    """
    id = models.IntegerField(primary_key=True)
    info = models.CharField(max_length=100)
    user_notes = models.CharField(max_length=200, blank=True) #user can set any info to this field
    # these are used in displaying user defined amount of data points
    datapoints = models.IntegerField(default=5)
    preference = models.BooleanField(default=False)

    # Alarms, from legacy reasons named warnings, should be alarms 

    dust_warnings = models.IntegerField(default=0) #this is used to detect if an alarm email needs to be send
    # this is the value which triggers alarms
    dust_set_point = models.IntegerField(default=20) 
    # this is user defined value that tells how many alarms lead to an alarm email and alarm
    dust_trigger = models.IntegerField(default=2)


    temp_warnings = models.IntegerField(default=0)
    temp_treshold = models.IntegerField(default=30)
    temp_trigger = models.IntegerField(default=2)

    humd_warnings = models.IntegerField(default=0)
    humd_treshold = models.IntegerField(default=60)
    humd_trigger = models.IntegerField(default=2)

    light_warnings = models.IntegerField(default=0)
    light_treshold = models.IntegerField(default=10000) #disabled with stardard settings
    light_trigger = models.IntegerField(default=2)

    # Warning tresholds, these can be configured separately and don't trigger an email nor alarm
    # all devices uses these to show warnings
    # light could also have one but seems unnecessary
    dust_warning = models.IntegerField(default=8)
    temp_warning = models.IntegerField(default=26)
    humd_warning = models.IntegerField(default=55)
    light_warning = models.IntegerField(default=10000) #disabled

    #Battery voltage, tresholds are not customisable by enduser
    volt_warning = models.FloatField(default=3.6)
    volt_alarm = models.FloatField(default=3.4)





    def __str__(self):
        return 'Device: {0}' .format(self.info)

class Data(models.Model):
    """
    Model representing one received measurement data.
    Values integers:
        collection_date: datetime value
        temperature: 0 - 99
        humidity: 0 - 99
        dust: 0 - 99 (not implemented)
        light: 0 - 9 (not implemented)
        voltage: 0 - 99 (not imlemented)
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE) # Link data to device
    collection_date = models.DateTimeField() # Date and time of data collected
    temperature = models.IntegerField()
    humidity = models.IntegerField()

    dust = models.IntegerField(null=True, blank=True)
    light = models.IntegerField(null=True, blank=True)
    voltage = models.FloatField(default=100.0) # this only to make logic easier to make


    def __str__(self):
        return 'Date: {0}, Temp: {1}, Device ID: ({2})' \
        .format(self.collection_date, self.temperature, self.device.info)

    # Converting model in to dict for API
    def as_dict(self):
        # Charts don't use default datetime format, so we need to change it
        date = self.collection_date.strftime("%Y-%m-%dT%H:%M:%S")
        return {
            'device': self.device.id,
            
            'dust_warning': self.device.dust_warning,
            'temp_warning': self.device.temp_warning, 
            'humd_warning': self.device.humd_warning,

            'date': date,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'dust': self.dust,
            'light': self.light,
        }

class Email(models.Model):
    # These models represent email addresses where warnings should be send to

    address = models.EmailField()
    devices = models.ManyToManyField(Device)
    device_name = models.CharField(max_length=100, null=True)
    
    

class Alarm(models.Model):
    # This class stores all triggered alarms
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alarm_type = models.CharField(max_length=200)
    time = models.DateTimeField()
    time_over = models.DateTimeField(null=True) #time when situation normalized
    time_ack = models.DateTimeField(null=True) #time when alarm was inactivated
    active = models.BooleanField(default = True) #tells whether alarms is active or not
    device_id = models.IntegerField(null=True) #link to device
    alarm= models.CharField(null=True, max_length=20) #dust, temp, humd, light, volts