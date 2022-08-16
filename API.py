import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from dao.Database import Read


@api_view(['''GET'''])
def get_counters(request):
    return HttpResponse(json.dumps(Read('''counters'''), default=lambda o: o.__dict__),
                        content_type='''application/json''')


@api_view(['''GET'''])
def TestimonialData(request):
    data = [
        {
            "id": 1,
            "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "author": "کاربر 1000",
            "authorThumb": "testimonial/h-2-t-01.png",
            "designation": "مدیر فنی فیسبوک"
        },
        {
            "id": 2,
            "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "author": "کاربر 2",
            "authorThumb": "testimonial/h-2-t-02.png",
            "designation": "موسس علی بابا"
        },
        {
            "id": 3,
            "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "author": "کاربر 3",
            "authorThumb": "testimonial/h-2-t-03.png",
            "designation": "مدیر اجرایی دیجی کالا"
        }
    ]

    return HttpResponse(json.dumps(data), content_type='''application/json''')


def SliderData(request):
    data = [
        {
            "id": 1,
            "title": "قالب ری اکت شرکتی",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-01.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        },
        {
            "id": 2,
            "title": "پول خود را هدر ندهید",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-02.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        }
    ]

    return HttpResponse(json.dumps(data), content_type='application/json')
